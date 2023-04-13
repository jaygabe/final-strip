import logging

from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from journal_apps.authentication.authentication import JWTAuthentication
from journal_apps.common.permissions import IsOwner
from journal_apps.common.utils import extract_data_and_assign_user, remove_empty_fields
from journal_apps.fencers.models import Fencer
from journal_apps.usaf_data.models import USAFencingInfo
from journal_apps.fencers.serializers import FencerSerializer, CreateFencerSerializer

User = get_user_model()

logger = logging.getLogger(__name__)


class FencerDetailView(APIView):
    # authentication_classes = [JWTAuthentication]
    serializer_class = FencerSerializer

    def get(self, request, slug):
        
        try:
            fencer = Fencer.object.get(slug=slug)
        except Fencer.DoesNotExist:
            NotFound("The fencer cannot be found.")
        
        serializer = FencerSerializer(fencer)
        return Response(serializer, status=status.HTTP_200_OK)


class FencerListView(generics.ListAPIView):
    permission_classes = [JWTAuthentication]
    serializer_class = FencerSerializer
    paginate_by = 10

    def get_queryset(self):
        print('request: ', self.request.__dict__)
        print('user: ', self.request.user)
        user = self.request.user
        fencers = Fencer.objects.filter(user=user)

        return fencers


class FencerCreateView(generics.CreateAPIView):
    permission_classes = [JWTAuthentication]
    serializer_class = CreateFencerSerializer

    def create(self, request):
        data = extract_data_and_assign_user(request)
        print('data: ', data)
        cleaned_data = remove_empty_fields(data)
        print('cleaned: ', cleaned_data)
        if 'member_id' in cleaned_data.keys():
            member_info = USAFencingInfo.objects.get(member_id=cleaned_data['member_id'])
            cleaned_data['usa_fencing_info'] = member_info.pk
            cleaned_data['first_name'] = member_info.first_name
            cleaned_data['last_name'] = member_info.last_name
        serializer = self.serializer_class(data=cleaned_data, context={"request": request})
        if serializer.is_valid(raise_exception=True):
            print('validated: ', serializer.validated_data)
            serializer.save()
            logger.info(
                f"fencer {serializer.data.get('last_name')}, {serializer.data.get('first_name')} created by {request.user.email}"
            )
            return Response({'message': 'Fencer created'}, status=status.HTTP_201_CREATED)

        print('serializer errors: ', serializer.errors)
        return Response({'message': 'invalid form error'}, status=status.HTTP_400_BAD_REQUEST)


class FencerUpdateView(APIView):
    # permission_classes = [JWTAuthentication, IsOwner]
    serializer_class = FencerSerializer

    def patch(self, request, slug):
        try:
            fencer = Fencer.objects.get(slug=slug)
        except Fencer.DoesNotExist:
            NotFound("The fencer cannot be found.")
        
        data = request.data
        serializer = self.serializer_class(fencer, data=data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

class FencerDeleteView(generics.DestroyAPIView):
    # permission_classes = [JWTAuthentication, IsOwner]
    queryset = Fencer.objects.all()
    lookup_field = "slug"

    def delete(self, request, *args, **kwargs):
        try:
            Fencer.objects.get(slug=self.kwargs.get("slug"))
        except Fencer.DoesNotExist:
            NotFound("The fencer cannot be found.")
        
        delete_operation = self.destroy(request)
        data = {}
        if delete_operation:
            data["success"] = "Delete successful"
        else:
            data["failure"] = "Delete failed"

        return Response(data=data)
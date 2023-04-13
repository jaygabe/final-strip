import logging

from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from journal_apps.authentication.authentication import JWTAuthentication
from journal_apps.bouts.models import Bout
from journal_apps.fencers.models import Fencer
from journal_apps.events.models import Event
from journal_apps.tournaments.models import Tournament
from journal_apps.bouts.serializers import BoutSerializer

from journal_apps.common.utils import extract_data_and_assign_user, remove_empty_fields

User = get_user_model()

logger = logging.getLogger(__name__)


class BoutDetailView(APIView):
    # authentication_classes = [JWTAuthentication]

    def get(self, request, slug):
        
        try:
            bout = Bout.objects.get(slug=slug)
        except Bout.DoesNotExist:
            NotFound("The bout cannot be found.")
        
        serializer = BoutSerializer(bout)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BoutListView(generics.ListAPIView):
    # permission_classes = [JWTAuthentication]
    serializer_class = BoutSerializer
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        bouts = Bout.objects.filter(user=user)

        return bouts


class BoutCreateView(generics.CreateAPIView):
    # permission_classes = [JWTAuthentication]
    serializer_class = BoutSerializer

    def create(self, request):
        data = extract_data_and_assign_user(request)
        cleaned_data = remove_empty_fields(data)
        fencer_a = Fencer.objects.get(slug=cleaned_data['fencer_a']).pkid
        fencer_b = Fencer.objects.get(slug=cleaned_data['fencer_b']).pkid
        event = Event.objects.get(slug=cleaned_data['event_slug']).pkid
        cleaned_data['fencer_a'] = Fencer.objects.get(slug=fencer_a).pkid
        cleaned_data['fencer_b'] = Fencer.objects.get(slug=fencer_b).pkid
        cleaned_data['event'] = event
        cleaned_data['tournament'] = Tournament.objects.get(slug=event).pkid
        print('cleaned up:  ', cleaned_data)


        # validate winner_is_a
        if cleaned_data['winner_is_a'] == None:
            Response({'message': 'WinnerIsA is required'}, status=status.HTTP_409_CONFLICT)
        if cleaned_data['score_a'] > cleaned_data['score_b'] and cleaned_data['winner_is_a'] == False:
            Response({'message': 'WinnerIsA mismatch'}, status=status.HTTP_409_CONFLICT)
        if cleaned_data['score_a'] < cleaned_data['score_b'] and cleaned_data['winner_is_a'] == True:
            Response({'message': 'WinnerIsA mismatch'}, status=status.HTTP_409_CONFLICT)
        
        serializer = self.serializer_class(data=cleaned_data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            logger.info(
                f"Bout {serializer.data.get('fencer_a')} vs {serializer.data.get('fencer_b')} created by {request.user.email}"
            )
            return Response({'message': 'Event created'}, status=status.HTTP_201_CREATED)

        print('serializer errors: ', serializer.errors)
        return Response({'message': 'invalid form error'}, status=status.HTTP_400_BAD_REQUEST)


class BoutUpdateView(APIView):
    # permission_classes = [JWTAuthentication, IsOwner]
    serializer_class = BoutSerializer

    def patch(self, request, slug):
        try:
            bout = Bout.objects.get(slug=slug)
        except Bout.DoesNotExist:
            NotFound("The bout cannot be found.")
        
        data = request.data
        serializer = self.serializer_class(bout, data=data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

class BoutDeleteView(generics.DestroyAPIView):
    # permission_classes = [JWTAuthentication, IsOwner]
    queryset = Bout.objects.all()
    lookup_field = "slug"

    def delete(self, request, *args, **kwargs):
        try:
            Bout.objects.get(slug=self.kwargs.get("slug"))
        except Bout.DoesNotExist:
            NotFound("The bout cannot be found.")
        
        delete_operation = self.destroy(request)
        data = {}
        if delete_operation:
            data["success"] = "Delete successful"
        else:
            data["failure"] = "Delete failed"

        return Response(data=data)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.db.models import Q

from journal_apps.usaf_data.models import USAFencingInfo
from journal_apps.usaf_data.serializer import USAFencingInfoSerializer, FencerRecordSerializer
from journal_apps.usaf_data.load_usa_fencing_membership import load_membership_data

@api_view(["GET"])
def manual_reload(request):
    
    if not request.user.is_superuser:
        return Response({'error: you cannot do that'}, status=status.HTTP_401_UNAUTHORIZED)

    load_membership_data()
    data = {
                'Testing': 'Data loaded', 
            }
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
def fencer_record(_, member_id):
    fencer = USAFencingInfo.objects.get(member_id=member_id)
    serializer = FencerRecordSerializer(fencer)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def query_usaf_fencers(_, query):
    fencer_data = USAFencingInfo.objects.filter(
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query)
        # | Q(member_id__iexact=query)
        )
    serializer = USAFencingInfoSerializer(data=fencer_data, many=True)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)

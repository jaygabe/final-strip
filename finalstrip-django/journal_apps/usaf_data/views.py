from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes


from journal_apps.usaf_data.load_usa_fencing_membership import load_membership_data

@api_view(["GET"])
def manual_reload(request):
    
    mem_data = load_membership_data()
    data = {
                'Testing': 'Data loaded', 
            }

    return Response(data, status=status.HTTP_200_OK)

# serialize one row

#serialze and paginate a list
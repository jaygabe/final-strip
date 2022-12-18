

from urllib import response
from rest_framework.views import exception_handler


#  changes the default exception in the rest_framework so that the APIException() does not return a 403 forbidden
#  code and instead a 401 unauthorized
#  changed also in settings.py
def status_code_handler(exc, context):
    # response = exception_handler(exc, context)

    # if response is not None and response.status_code == 403: 
    #     print('secretly 403')
    #     response.status_code = 401
    
    # return response
    pass


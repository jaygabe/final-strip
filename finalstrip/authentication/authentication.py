from logging import exception
import jwt, datetime
from rest_framework import exceptions

# abstract class view imports
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from .models import User

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        
        auth = get_authorization_header(request).split()
        #  
        # cookie_headers = request.headers['Cookie'].split()
        # print(cookie_headers)
        # cookie_dic = {}
        # for cookie_string in cookie_headers:

        #     pair = cookie_string.split('=')
        #     cookie_dic[pair[0]] = pair[1]
        # print('cookie dic', cookie_dic)
        # auth = ['filler string to maintain the rest', cookie_dic['refresh_token']]

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = User.objects.get(pk=id)

            return (user, None)
        raise exceptions.AuthenticationFailed('jwt unauthenticated')



def create_access_token(id):
    return jwt.encode({
        'user_id': id, 
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=120), 
        'iat': datetime.datetime.utcnow()  
    }, 'access_secret', algorithm='HS256')

def create_refresh_token(id):
    return jwt.encode({
        'user_id': id, 
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7), 
        'iat': datetime.datetime.utcnow()  
    }, 'refresh_secret', algorithm='HS256')

def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms='HS256') # note that algorithms has an 's' here
        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')

def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256') # note that algorithms has an 's' here
        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')
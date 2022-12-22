from logging import exception
import jwt, datetime
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header

User = get_user_model()

# uses access token from request header to authenticate user
class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = User.objects.get(pk=id)

            return (user, None)
        raise exceptions.AuthenticationFailed('jwt unauthenticated')
    
    # this should allow other views to work now
    def has_permission(self, request, view):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)
            user = User.objects.get(pk=id)
            request.user.id = user.id
            return True
        return False

def create_access_token(id):
    return jwt.encode({
        'user_id': id, 
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=120), 
        'iat': datetime.datetime.utcnow()  
    }, 'access_secret', algorithm='HS256')

def create_refresh_token(id):
    return jwt.encode({
        'user_id': id, 
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=10), 
        'iat': datetime.datetime.utcnow()  
    }, 'refresh_secret', algorithm='HS256')

def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms='HS256')
        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')

def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256')
        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')
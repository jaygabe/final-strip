import datetime, random, string
import pyotp

from google.oauth2 import id_token
from google.auth.transport.requests import Request as GoogleRequest

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions, status

from .models import Reset, User, UserToken
from .serializers import UserSerializer
from .authentication import create_access_token, create_refresh_token, decode_refresh_token, JWTAuthentication


class RegisterAPIView(APIView):
    def post(self, request):

        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Passwords do not match!')
        
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True) # makes sure all fields are present
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.get(email=email)
    
        # check if email is in database
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid credentials')
        
        # check is password matches email
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Invalid credentials')

        # if mfa is enabled then follow along with MFA
        if user.require_mfa:
            if user.tfa_secret:
                return Response({
                    'id': user.id
                })

            secret = pyotp.random_base32()  # used to generate the QR code
            otpauth_url = pyotp.totp.TOTP(secret).provisioning_uri(issuer_name='My App') # 'My App' will be displayed in the authenticator

            # email is not activated so printing code to console
            print('SECRET CODE: ', secret)
            print('2FA URL: ', otpauth_url)

            return Response({
                'id': user.id,
                'secret': secret,
                'otpauth_url': otpauth_url
            })
        
        else:
            # create tokens
            access_token = create_access_token(user.id)
            refresh_token = create_refresh_token(user.id)

            # creates a table of tokens handed out to block if needed
            UserToken.objects.create(
                user_id=user.id,
                token=refresh_token,
                expired_at=datetime.datetime.utcnow() + datetime.timedelta(days=7)
            )

            response = Response()
            # setting the cookie to http-only will keep the cookie on the backend
            response.set_cookie(key='refresh_token', value=refresh_token, httponly=True) 

            response.data = {
                'token': access_token
            }

            return response
        
        
        return Response({'Bad Request':'Login Error'}, status=status.HTTP_400_BAD_REQUEST)
        

class TwoFactorAPIView(APIView):
    def post(self, request):
        
        id = request.data['id']

        user = User.objects.filter(pk=id).first()

        if not user:
            raise exceptions.AuthenticationFailed('Invalid credentials')

        # assign or create secret
        secret = user.tfa_secret if user.tfa_secret !='' else request.data['secret']

        # check against code send through the QR code for the phone
        if not pyotp.TOTP(secret).verify(request.data['code']):
            raise exceptions.AuthenticationFailed('Invalid credentials')

        # save secret in user
        if user.tfa_secret == '':
            user.tfa_secret = secret
            user.save()

        # create tokens
        access_token = create_access_token(id)
        refresh_token = create_refresh_token(id)

        # creates a table of tokens handed out to block if needed
        UserToken.objects.create(
            user_id=id,
            token=refresh_token,
            expired_at=datetime.datetime.utcnow() + datetime.timedelta(days=7)
        )

        response = Response()
        # setting the cookie to http-only will keep the cookie on the backend
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True) 

        response.data = {
            'token': access_token
        }

        return response


class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    
    def get(self, request):
        return Response(UserSerializer(request.user).data)


class RefreshAPIView(APIView):
    def post(self, request):
        
        refresh_token = request.COOKIES.get('refresh_token')

        id = decode_refresh_token(refresh_token)

        if not UserToken.objects.filter(
            user_id=id,
            token=refresh_token,
            expired_at__gt=datetime.datetime.now(tz=datetime.timezone.utc)
        ).exists():
            raise exceptions.AuthenticationFailed('unauthenticated refresh token errors')

        access_token = create_access_token(id)

        return Response({
            'token': access_token
        })


class LogoutAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    
    def post(self, request):
        UserToken.objects.filter(user_id=request.user.id).delete()

        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data = {
            'message': 'success'
        }

        return response


class ForgotAPIView(APIView):
    def post(self, request):
        token = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))

        Reset.objects.create(
            email=request.data['email'],
            token=token
        )
        
        print('reset token:  ', token)

        # email = request.data['email']
        # url = '127.0.0.1:8000/reset/' + token

        # # send email
        # send_mail(
        #     subject='Reset Password', # subject
        #     message=f'Click <a href="{url}">here</a> to reset your password!', # message
        #     from_email='justin107d@gmail.com', # from address
        #     recipient_list=[email], # to email address
        # )

        return Response({
            'message': 'success'
        })


class ResetAPIView(APIView):
    def post(self, request):

        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Passwords do not match!')
        
        reset_password = Reset.objects.filter(tokens=data['token']).first()

        if not reset_password:
            raise exceptions.APIException('Invalid link!')
        
        user = User.objects.filter(email=reset_password.email).first()

        if not user:
            raise exceptions.APIException('User not found!')

        user.set_password(data['password'])
        user.save()

        return Response({
            'message': 'success'
        })


class GoogleAuthAPIView(APIView):
    
    def post(self, request):

        
        token = request.data['token']
        
        google_user = id_token.verify_token(token, GoogleRequest()) # verifies token with Google

        if not google_user:
            raise exceptions.AuthenticationFailed('unauthenticated')
        
        user = User.objects.filter(email=google_user['email']).first()

        if not user:
            user = User.objects.create(
                first_name=google_user['given_name'],
                last_name=google_user['family_name'],
                email=google_user['email']
            )
            
            user.set_password(token)
            user.save()

        # create tokens
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        # creates a table of tokens handed out to block if needed
        UserToken.objects.create(
            user_id=user.id,
            token=refresh_token,
            expired_at=datetime.datetime.utcnow() + datetime.timedelta(days=7)
        )

        response = Response()
        # setting the cookie to http-only will keep the cookie on the backend
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True) 

        response.data = {
            'token': access_token
        }

        return response
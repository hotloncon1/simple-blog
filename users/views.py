from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from .serializers import UserSerializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken, SlidingToken


# Create your views here.

class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class List(APIView):
    def get(self, request):
        users = [User.objects.all()]
        serializer = UserSerializer(users)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            return Response({'message': 'User not found!'}, status=status.HTTP_401_UNAUTHORIZED)
        if not user.check_password(password):
            return Response({'message': 'Password is incorrect!'},
                            status=status.HTTP_401_UNAUTHORIZED)
        # SlidingToken.for_user(user)
        # RefreshToken.for_user(user)
        token = {
            'access': str(RefreshToken.for_user(user).access_token),
            'refresh': str(RefreshToken.for_user(user))
        }
        return Response(
            {'message': 'success', 'token': token}, status=status.HTTP_200_OK)

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ManagerLoginSerializer, UserRegisterSerializer, ManagerSerializer
from managers.models import Manager


class ManagerRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            email=serializer.validated_data['email']
        )
        manager = Manager.objects.create(user=user, phone=serializer.validated_data['phone'])
        manager.save()
        return Response(data={'id': manager.id}, status=status.HTTP_201_CREATED)


class ManagerLoginAPIView(APIView):
    def post(self, request):
        serializer = ManagerLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error': 'Invalid user or password'})


class ManagerListAPIView(ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class =ManagerSerializer
    #permission_classes = [IsAuthenticated]


class ManagerDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    #permission_classes = [IsAuthenticated]
    lookup_field = "id"


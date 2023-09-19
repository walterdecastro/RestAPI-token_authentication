from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from register.models import Register
from rest_api.serializers import RegisterModelSerializer


class RegisterModelViewSet(ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterModelSerializer
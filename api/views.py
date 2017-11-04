from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from django.contrib import auth
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from django.views.generic import View
from hiren import settings
from django.http import HttpResponse
import os
import logging


def login(request):
    """
    token authentication for api
    :param request:
    :return:
    """
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            token = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': str(token[0])}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'Username/Password is not valid'}, status=status.HTTP_401_UNAUTHORIZED)

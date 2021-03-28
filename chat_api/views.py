from django.db import models
from django.shortcuts import render
from django.http.response import HttpResponse

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from .models import Message
from .serializers import MessageSerializer

# Create your views here.


def index(request):
    
    return HttpResponse('<h1>Go to <a href="/api/v1/messages/list/">/api/v1/messages/list/</a> URI</h1>')


class MessagesPaginatedListView(ListAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class SingleMessageView(RetrieveAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class CreateMessageView(CreateAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
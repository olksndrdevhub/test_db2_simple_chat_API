from django.db import models
from django.shortcuts import render
from django.http.response import HttpResponse

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from .models import Message
from .serializers import MessageSerializer

# Create your views here.


def index(request):
    
    return HttpResponse('<h1>Index Page for Simple_Chat API<br> Go to <a href="swagger-ui">swagger-ui/</a> to test API</h1>')


class MessagesPaginatedListView(ListAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class SingleMessageView(RetrieveAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class CreateMessageView(CreateAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
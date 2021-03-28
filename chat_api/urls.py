from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view


from .views import index, MessagesPaginatedListView, SingleMessageView, CreateMessageView

urlpatterns = [

    path('', index, name="index_view"),
    path('api/v1/messages/list/', MessagesPaginatedListView.as_view(), name='messages_list'),
    path('api/v1/messages/single/<int:pk>', SingleMessageView.as_view(), name='message_single'),
    path('api/v1/messages/create/', CreateMessageView.as_view(), name='message_create'),

    path('openapi', get_schema_view(
            title="Simple Chat",
            description="API for public chat",
            version="1.0.0"
        ), name='openapi-schema'),


    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),

]

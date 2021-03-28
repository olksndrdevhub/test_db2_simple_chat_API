from django.urls import path, include


from .views import index, MessagesPaginatedListView, SingleMessageView, CreateMessageView

urlpatterns = [

    path('', index, name="index_view"),
    path('api/v1/messages/list/', MessagesPaginatedListView.as_view(), name='messages_list'),
    path('api/v1/messages/single/<int:pk>', SingleMessageView.as_view(), name='message_single'),
    path('api/v1/messages/create/', CreateMessageView.as_view(), name='message_create'),

]

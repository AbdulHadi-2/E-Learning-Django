
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<int:chat_room_id>/', consumers.ChatConsumer.as_asgi()),
]
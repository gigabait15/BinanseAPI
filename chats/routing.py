from django.urls import re_path
from chats.consumers import BinanceConsumer

websocket_urlpatterns = [
    re_path(r'ws/binance/$', BinanceConsumer.as_asgi()),
]

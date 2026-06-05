from typing import Any, cast

from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # re_path(r"ws/chat/room/(?P<course_id>\d+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(
        r"ws/chat/room/(?P<course_id>\d+)/$",
        cast(Any, consumers.ChatConsumer.as_asgi()),
    ),
]

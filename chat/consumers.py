import json

from channels.generic.websocket import AsyncWebsocketConsumer

# from asgiref.sync import async_to_sync
from django.utils import timezone


class ChatConsumer(AsyncWebsocketConsumer):
    # async def connect(self):
    #     # self.user = self.scope["user"]
    #     self.user = self.scope.get("user")
    #     # self.id = self.scope["url_route"]["kwargs"]["course_id"]
    #     url_route = self.scope.get("url_route") or {}
    #     kwargs = url_route.get("kwargs") or {}
    #     self.id = kwargs.get("course_id")

    #     self.room_group_name = f"chat_{self.id}"

    #     # join room group
    #     await self.channel_layer.group_add(self.room_group_name, self.channel_name)
    #     # accept connection
    #     await self.accept()

    async def connect(self):
        self.user = self.scope.get("user")
        kwargs = (self.scope.get("url_route") or {}).get("kwargs") or {}
        self.id = kwargs.get("course_id")
        if not self.id:
            await self.close()
            return
        self.room_group_name = f"chat_{self.id}"
        if self.channel_layer is None:
            raise Exception("Redis / CHANNEL_LAYERS not configured")
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        now = timezone.now()

        username = getattr(self.user, "username", "Anonymous") or "Anonymous"

        # send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "user": username,
                "datetime": now.isoformat(),
            },
        )

    # receive message from room group
    async def chat_message(self, event):
        # send message to WebSocket
        await self.send(text_data=json.dumps(event))

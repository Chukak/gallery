import json
from image_gallery.models import ImageModel
from django.core.serializers.json import DjangoJSONEncoder
from channels.generic.websocket import WebsocketConsumer


class ImageLoadConsumer(WebsocketConsumer):
    """
    Image load consumer.
    Loads the number of images on url. self.count_images - number images

    Has 3 methods:
    1. connect - connects to websocket, open connection.
    2. receive - set the number if images and send it to url.
    3. disconnect - close connection.

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count_images = 0

    def connect(self):
        self.accept()
        self.count_images += 6

    def receive(self, text_data=None, bytes_data=None):
        # generator in the format [{attribute: value} for in objects[count:count+6]]
        result = [
            {
                "path": obj.path_to_image.url,
                "datetime": obj.datetime.strftime("%d %B %Y in %H:%M"),
                "size": obj.size,
                "name": obj.name,
            }
            for obj in
            ImageModel.objects.all().order_by("-datetime")[self.count_images: self.count_images + 6]
        ]
        self.send(json.dumps(
            result, cls=DjangoJSONEncoder
        ))

    def disconnect(self, close_code):
        self.count_images = 0
        self.close()

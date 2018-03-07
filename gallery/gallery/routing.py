from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from image_gallery.consumers import ImageLoadConsumer

# websocket router at path r'^$'
application = ProtocolTypeRouter({
    'websocket': URLRouter([
        url(r'^$', ImageLoadConsumer),
    ])
})
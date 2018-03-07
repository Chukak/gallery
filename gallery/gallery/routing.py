from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter


application = ProtocolTypeRouter({
    "websocket": URLRouter([

    ]),
})

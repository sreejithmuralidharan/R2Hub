from django.urls import path
from django.conf.urls import include
from . views import webhook_listener

app_name = 'api'
urlpatterns = [
    path('collection/<int:collection_id>',
         webhook_listener, name='webhook-listener'),
    path('auth', include('rest_framework.urls'))
]


from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings


from .views import home_page, api_request_page, collection_page


urlpatterns = [
    path('', home_page, name='home'),
    path('<int:organization_id>/collection',
         collection_page, name='collections'),
    path('<int:organization_id>/collection/<int:collection_id>',
         api_request_page, name='api_request'),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

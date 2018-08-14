
from django.conf.urls import *
from django.contrib import admin
from vipo import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin-principal/', admin.site.urls),
    url(r'^', include('adminvipo.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


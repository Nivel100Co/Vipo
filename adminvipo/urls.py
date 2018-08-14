from django.conf.urls import *
from adminvipo import views

urlpatterns = [
    url(r'^$',views.index.as_view(), name = 'index'),
    url(r'^register/',views.register.as_view(), name = 'register'),
    url(r'^login/',views.login.as_view(), name = 'login'),
]

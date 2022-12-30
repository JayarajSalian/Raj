from django.urls import path
from appx.views import *
app_name='Jay'
urlpatterns=[
    path('Jay/', Jay, name='Jay')
]
from django.urls import path
from app.views import *

app_name='app'
urlpatterns=[
    path('app_hi/',app_hi,name='app_hi'),
]
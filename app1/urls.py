from django.urls import path
from app1.views import *

app_name='app1'
urlpatterns=[
    path('app1_hi/',app1_hi,name='app1_hi'),
]
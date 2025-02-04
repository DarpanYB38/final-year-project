from django.urls import path
from crime_app.views import *

urlpatterns = [
    path('',crime_list, name='crime_list'),
    path('news/',fetch_news,name='fetch_news'),
]
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import routineList, routineDetail

urlpatterns = [
    path('routine', routineList),
    path('routine/<int:routine_id>', routineDetail),
    path('routine/result')
]
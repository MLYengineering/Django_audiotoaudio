from django.urls import path
from livekit_app import views


urlpatterns = [
	    path('', views.room_view, name='index'),
	]

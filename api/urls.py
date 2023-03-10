from .views import RegisterAPI, LoginAPI, VideoGameList
from django.urls import path, include
from knox import views as knox_views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('videos', viewset=VideoGameList)

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    # video game urls
    path('', include(router.urls)),

]
from django.urls import include, path
from knox import views as knox_views
from rest_framework import routers

from .views import LoginAPI, RegisterAPI, ReviewList, VideoGameList

router = routers.DefaultRouter()

router.register("videos", viewset=VideoGameList)
router.register("reviews", viewset=ReviewList)

urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register"),
    path("login/", LoginAPI.as_view(), name="login"),
    path("logout/", knox_views.LogoutView.as_view(), name="logout"),
    path("logoutall/", knox_views.LogoutAllView.as_view(), name="logoutall"),
    # video game urls
    path("", include(router.urls)),
]

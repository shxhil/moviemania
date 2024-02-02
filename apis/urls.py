from django.urls import path
from apis import views

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("movies",views.MovieView,basename="movies")

router.register("profile",views.ProfileViewset,basename="profile")

router.register("review",views.ReviewView,basename="review")

urlpatterns=[
    path("register/",views.SignUpView.as_view()),
    path("token/",ObtainAuthToken.as_view())
]+router.urls
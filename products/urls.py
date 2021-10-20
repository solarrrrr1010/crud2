from django.urls import path
from .views import ActorView, MovieView, ActorMovieView

urlpatterns = [
    path("Actor", ActorView.as_view()),
    path("Movie", MovieView.as_view()),
    path("ActorMovie", ActorMovieView.as_view())
]

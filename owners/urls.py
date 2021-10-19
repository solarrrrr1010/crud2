from django.urls import path
from .views import DogView, OwnerView

urlpatterns = [
    path("Owner", OwnerView.as_view()),
    path("Dog", DogView.as_view())
]


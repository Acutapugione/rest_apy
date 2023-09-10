from django.urls import path, include
from .views import (
    WebserviseListApiView,
    InfoApiView,
    WelcomeApiView,
    ArifmeticApiView,
    ExponentiationApiView,
)

urlpatterns = [
    path('api',WebserviseListApiView.as_view() ),
    path('welcome', WelcomeApiView.as_view()),
    path('arifmetic', ArifmeticApiView.as_view()),
    path('pow', ExponentiationApiView.as_view()),
    path('', InfoApiView.as_view()),
]

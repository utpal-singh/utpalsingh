from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "covid19homepage"),
    path('dev/', views.development, name = "dev")
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "homepage"),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name = "contact"),
    path('googlea3fa796d88ba8a2b.html', views.google_verification, name="google_verification"),
    path('cite', views.cite, name = 'cite')
]

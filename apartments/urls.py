from django.urls import path
from . import views


urlpatterns = [
    path('apartments/', views.ApartmentListAPIView.as_view()),
    path('apartments/<int:id>/', views.ApartmentDetailAPIView.as_view()),
]

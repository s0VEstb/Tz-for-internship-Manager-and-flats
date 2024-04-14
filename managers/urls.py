from django.urls import path
from .views import ManagerLoginAPIView, ManagerRegistrationAPIView, ManagerListAPIView, ManagerDetailAPIView

urlpatterns = [
    path('manager/login/', ManagerLoginAPIView.as_view()),
    path('manager/register/', ManagerRegistrationAPIView.as_view()),
    path('manager/', ManagerListAPIView.as_view()),
    path('manager/<int:id>/', ManagerDetailAPIView.as_view()),
]
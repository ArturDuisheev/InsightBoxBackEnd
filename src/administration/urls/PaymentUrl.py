from django.urls import path

from administration.api import views

urlpatterns = [
    path('status-and-create/', views.PaymentRequestAPIView.as_view(), name='create-and-status')
]
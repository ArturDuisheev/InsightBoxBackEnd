from django.urls import path

from administration.api import views

urlpatterns = [
    path('create/', views.PaymentRequestAPIView.as_view(), name='create'),
    path('status/<int:payment_id>/', views.GetPaymentStatusAPIView.as_view(), name='status')
]
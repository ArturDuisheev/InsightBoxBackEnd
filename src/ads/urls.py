from django.urls import path

from ads.api import views

urlpatterns = [
    path('list/', views.AdListAPIView.as_view(), name='ads_list'),
]
from django.urls import path

from profiles.api import views

urlpatterns = [
    path('list/', views.ProfileListAPIView.as_view(), name='profile-list'),
    path('edit/<str:user_id>/', views.ProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-retrieve-update')
]
from django.urls import path

from meditation.api import views

urlpatterns = [
    path('list-create/', views.MeditationListCreateAPIView.as_view(), name='list-create'),
    path('edit/', views.MeditationRetrieveUpdateDestroyAPIView.as_view(), name='edit'),
    path('contact_settings/', views.ContactSettingListAPiView.as_view(), name='contact_settings'),
]
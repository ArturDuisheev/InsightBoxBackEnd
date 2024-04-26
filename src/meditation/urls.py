from django.urls import path

from meditation.api import views

urlpatterns = [
    path('list-create/', views.MeditationListCreateAPIView.as_view(), name='list-create'),
    path('edit/', views.MeditationRetrieveUpdateDestroyAPIView.as_view(), name='edit')
]
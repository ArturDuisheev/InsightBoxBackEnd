from django.urls import path

from meditation.api import views

urlpatterns = [
    path('list-create/', views.MeditationListCreateAPIView.as_view(), name='list-create'),
    path('card/list/', views.MetaforicalCardListAPIVew.as_view(), name='card-list'),
    path('money_card/list/', views.MoneyMetaphoricalCardListAPIView.as_view(), name='money-card-list'),
    path('favorite/card/<int:pk>/', views.MetaforicalCardLikeAPIView.as_view(), name='card-favorites'),
    path('favorite/<int:pk>/', views.MeditationLikeAPIView.as_view(), name='meditation-favorites'),
    path('contact_settings/', views.ContactSettingListAPiView.as_view(), name='contact_settings'),
]
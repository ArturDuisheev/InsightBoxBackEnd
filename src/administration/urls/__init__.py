from django.urls import path, include
from . import PaymentUrl

urlpatterns = [
    path('actions/', include(PaymentUrl)),

]
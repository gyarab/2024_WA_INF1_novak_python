from django.urls import path
from .views import home, experimental

urlpatterns = [
  path('', home, name='home'),
  path('experimental/', experimental, name='experimental'),
]
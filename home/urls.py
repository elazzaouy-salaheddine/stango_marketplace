from django.urls import path
from .views import Home, AboutUs


urlpatterns = [
    path('', Home, name='home_page'),
    path('about/', AboutUs, name='about_us')
]

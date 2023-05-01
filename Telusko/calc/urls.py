from django.urls import path
from calc.views import home

urlpatterns = [
    path('home/', home, name='home'),
]

from django.urls import path
from . import views
url_pattern=[
          path('',views.home,name='home')

]
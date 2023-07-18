from django.urls import path
from . import views # . means from current directory import views.py


urlpatterns=[
  path('', views.index, name='index'), #user comes to ''url and views.index is whats going to be rendered
  path('pictures/', views.pictures, name='pictures'), #once they click a button they go to this view
  path('about/', views.about),
]

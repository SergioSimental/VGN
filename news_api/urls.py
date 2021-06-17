from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('archive', views.archive, name='archive'),
    path('search', views.search, name='search')
]

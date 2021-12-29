from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_url', views.create, name='create'),
    path('<slug:shortUrl>', views.redirect_url, name='redirect'),
]
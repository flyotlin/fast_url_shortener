from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_url, name='index'),
    path('create_url', views.create_short_url, name='create'),
    path('<slug:shortUrl>', views.redirect_url, name='redirect'),
]
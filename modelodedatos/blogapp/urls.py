from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.mostrar_posts, name='mostrar_post'),
]

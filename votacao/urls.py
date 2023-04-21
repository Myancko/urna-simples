from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('home/', views.home, name='Home'),
    path('votar/<int:id>', views.vote, name='Vote'),
    path('criar/', views.criar_votacao, name='Criar'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
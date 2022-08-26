from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('rapiexpress', views.rapiexpress, name='rapiexpress'),
    path('crear', views.crear, name='crear'),
    path('login', views.login, name='login'),
    path('nosotros', views.nosotros, name='nosotros'),
]

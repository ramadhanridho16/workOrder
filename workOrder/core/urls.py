from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',
         authentication_form=LoginForm), name='login'),
    path('', views.work_list, name='work_list'),
    path('core/<int:pk>/', views.work_detail, name='work_detail'),
    path('core/new/', views.work_create, name='work_create'),
    path('core/<int:pk>/edit/', views.work_update, name='work_update'),
    path('core/<int:pk>/delete/', views.work_delete, name='work_delete'),
    path('core/cetak/', views.cetak, name='cetak'),
    path('core/search/', views.work_search, name='work_search'),
    path('core/download/excel', views.download_excel, name='download_excel'),
]
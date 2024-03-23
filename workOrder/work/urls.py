from django.urls import path

from . import views

app_name = 'work'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path("work/", views.index, name='index')
]

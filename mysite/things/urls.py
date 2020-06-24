from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<int:thing_id>/update/', views.update, name='update'),
    path('<int:thing_id>/delete/', views.delete, name='delete'),
]
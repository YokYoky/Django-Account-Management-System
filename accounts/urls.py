from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:id>', views.view_account, name='view_account'),
  path('add/', views.add_account, name='add_account'),
  path('update/<int:id>/', views.update, name='update'),
  path('delete/<int:id>/', views.delete, name='delete'),
  path('search/', views.search_account, name='search_account'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('randomrecipe/', views.recipe),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>/', views.detail, name='detail'),

]

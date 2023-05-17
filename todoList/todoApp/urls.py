from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoList, name='todoList'),
    path('<int:pk>/', views.todoDetail, name='todoDetail'),
    path('post/', views.todoPost, name='todoPost'),
    path('<int:pk>/edit/', views.todoEdit, name='todoEdit'),
    path('done/', views.todoDoneList, name='todoDoneList'),
    path('done/<int:pk>', views.todoDone, name='todoDone'),
    path('<int:pk>/ListDelete/', views.todoDeleteFromList, name='todoDelete'),
    path('<int:pk>/DoneDelete/', views.todoDeleteFromDone, name='todoDelete'),
]
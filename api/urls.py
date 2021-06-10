from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name = "api-overview"),
    path('task-list/', views.taskList, name = "task-list"),
    path('task-create/', views.taskCreate, name = "task-create"),
    path('task-details/<str:pk>', views.taskDetail, name = "task-details"),
    path('task-Update/<str:pk>', views.taskUpdate, name = "task-Update"),
    path('task-Delete/<str:pk>', views.taskDelete, name = "task-Delete")
    ]
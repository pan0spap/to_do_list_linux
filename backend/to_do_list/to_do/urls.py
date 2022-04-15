from django.urls import path
from . import views


urlpatterns = [
    path('taskslist/', views.tasks_list),
    path('taskslist/<int:pk>', views.tasks_detail),
]
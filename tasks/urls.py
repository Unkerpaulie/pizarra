from django.urls import path
from . import views

app_name = "tasks"


urlpatterns = [
    path('new/', views.new_task, name="new_task"),
    path('<uuid:task_id>/delete/', views.delete, name="delete"),
    path('<uuid:task_id>/edit/', views.edit, name="edit"),
    path('<uuid:task_id>/done/', views.done, name="done"),
]

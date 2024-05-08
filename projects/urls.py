from django.urls import path, include
from . import views

app_name = "projects"


urlpatterns = [
    path('', views.home, name="projects"),
    path('new/', views.new_project, name="new_project"),
    path('<uuid:pk>/', views.details, name="details"),
    path('<uuid:pk>/edit/', views.edit, name="edit"),
    path('<uuid:pk>/delete/', views.delete, name="delete"),
    path('<uuid:proj_id>/tasks/', include("tasks.urls")),
    path('<uuid:proj_id>/notes/', include("notes.urls")),
]

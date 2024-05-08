from django.urls import path
from . import views

app_name = "notes"


urlpatterns = [
    path('', views.home, name="home"),
    path('new/', views.new_note, name="new_note"),
    path('<uuid:note_id>/delete/', views.delete, name="delete"),
    path('<uuid:note_id>/edit/', views.edit, name="edit"),
]

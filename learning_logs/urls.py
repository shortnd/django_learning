""" Defines URL patterns for learning_logs. """
from django.urls import path
from . import views

urlpatterns = [
  # Home page
  path('', views.index, name="index"),
  path('topics/', views.topics, name="topics"),
  path('topics/<int:topic_id>/', views.topic, name="topic"),
  path('new-topics/', views.new_topic, name="new-topic"),
  path('new-entry/<int:topic_id>/', views.new_entry, name="new-entry"),
  path('edit-entry/<int:entry_id>/', views.edit_entry, name="edit-entry"),
]

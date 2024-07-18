# flashcards/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_view, name='quiz'),
    path('topics/<str:topic>/', views.quiz_questions_by_topic, name='quiz_questions_by_topic'),
    path('question/<int:pk>/', views.quiz_question, name='quiz_question'),
    path('add/', views.add_question, name='add_question'),
]

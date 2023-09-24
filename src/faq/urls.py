from django.urls import path
from . import views

urlpatterns = [
    path("", views.question_list, name="question_list"),
    path("question/<int:pk>", views.question_detail, name="question_detail"),
    path("question/<int:pk>/edit", views.question_edit, name="question_edit"),
    path("question/new/", views.question_new, name="question_new"),
]

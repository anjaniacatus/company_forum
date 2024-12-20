from django.urls import path
from . import views

urlpatterns = [
    path("", views.question_list, name="question_list"),
    path("question/search", views.question_search, name="question_search"),
    path("question/<int:pk>", views.question_detail, name="question_detail"),
    path("question/<int:pk>/edit", views.answer_edit, name="answer_edit"),
    path("question/new/", views.question_new, name="question_new"),
    path("guest_question/<int:pk>/edit", views.question_edit, name="question_edit"),
    path("question/<pk>/resolve/", views.question_resolve, name="question_resolve"),
    path("question/<pk>/publish/", views.question_publish, name="question_publish"),
    path("about", views.faq_about, name="faq_app_about"),
    path(
        "question/published",
        views.my_published_questions,
        name="my_published_questions",
    ),
    path("question/my_drafts", views.my_drafts, name="my_drafts"),
    path(
        "question/non_resolved_guest_questions",
        views.non_resolved_guest_questions,
        name="non_resolved_guest_questions",
    ),
    path("question/all_resolved", views.question_list, name="all_resolved_questions"),
    path(
        "question/non_resolved",
        views.non_resolved_questions,
        name="non_resolved_questions",
    ),
]

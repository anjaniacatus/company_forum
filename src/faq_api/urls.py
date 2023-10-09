from django.urls import path

from . import views

urlpatterns = [path(r"faq/api/v1/questions", views.QuestionList.as_view())]

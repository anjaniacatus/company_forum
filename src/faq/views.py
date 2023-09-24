from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Question


def question_list(request):
    questions = Question.objects.all().order_by("created_date")
    paginator = Paginator(questions, 3)
    # page_number = request.GET.get("page")
    page_number = 1
    questions_per_page = paginator.get_page(page_number)
    return render(
        request,
        "../templates/pages/question_list.html",
        {"questions_per_page": questions_per_page},
    )

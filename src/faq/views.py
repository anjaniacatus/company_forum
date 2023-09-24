from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Question
from .forms import QuestionForm


def question_list(request):
    questions = (
        Question.objects.all()
        .filter(resolved_date__isnull=False)
        .order_by("created_date")
    )
    paginator = Paginator(questions, 3)
    # page_number = request.GET.get("page")
    page_number = 1
    questions_per_page = paginator.get_page(page_number)
    return render(
        request,
        "../templates/pages/question_list.html",
        {"questions_per_page": questions_per_page},
    )


def question_new(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect("question_detail", pk=question.pk)
    else:
        form = QuestionForm()
        return render(request, "../templates/faq/question_edit.html", {"form": form})


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(
        request, "../templates/faq/question_detail.html", {"question": question}
    )


@login_required
def question_edit(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect("question_detail", pk=question.pk)
    else:
        form = QuestionForm(instance=question)
    return render(request, "../templates/faq/question_edit.html", {"form": form})


@login_required
def question_resolve(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.resolve()
    return redirect("question_detail", pk=pk)

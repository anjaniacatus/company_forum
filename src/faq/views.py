from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Question
from .forms import QuestionForm, AnswerForm
from QuestionBox.helpers import question_filter


def paginate(request, questions):
    paginator = Paginator(questions, 3)
    page = request.GET.get("page", 1)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return questions


def question_list(request):
    questions = question_filter.when_resolved_date_is_not_null()
    print(questions)
    return render(
        request,
        "../templates/pages/question_list.html",
        {"questions": paginate(request, questions), "title": "Home"},
    )


@login_required
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
def answer_edit(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect("question_detail", pk=question.pk)
    else:
        form = AnswerForm(instance=question)
    return render(
        request,
        "../templates/faq/answer_edit.html",
        {"form": form, "question": question},
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
    return render(
        request,
        "../templates/faq/question_edit.html",
        {"form": form, "question": question},
    )


@login_required
def question_resolve(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.resolve()
    return redirect("question_detail", pk=pk)


@login_required
def question_publish(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.publish()
    return redirect("question_detail", pk=pk)


@login_required
def my_published_questions(request):
    questions = question_filter.by_author_and_published_date_is_not_null(request)
    return render(
        request,
        "../templates/pages/question_list.html",
        {
            "questions": paginate(request, questions),
            "title": "Mes questions publiées sur le site",
        },
    )


@login_required
def my_drafts(request):
    questions = question_filter.by_author_and_published_date_is_null(request)
    return render(
        request,
        "../templates/pages/question_list.html",
        {"questions": paginate(request, questions), "title": "Brouillons"},
    )


@login_required
def non_resolved_questions(request):
    questions = (
        question_filter.when_published_date_is_not_null_and_resolved_date_is__null()
    )
    return render(
        request,
        "../templates/pages/question_list.html",
        {"questions": paginate(request, questions), "title": "Questions à Traiter"},
    )


@login_required
def non_resolved_guest_questions(request):
    questions = question_filter.by_author_and_resolved_date_is_null(request)
    return render(
        request,
        "../templates/pages/question_list.html",
        {
            "questions": paginate(request, questions),
            "title": "Mes questions en attente de réponse",
        },
    )


def question_search(request):
    if request.method == "POST":
        questions = question_filter.by_keywords(request)
        return render(
            request,
            "../templates/faq/question_search.html",
            {
                "questions": questions,
                "title": "Home",
                "key_searched": request.POST["key_searched"],
            },
        )
    else:
        return redirect("question_list")

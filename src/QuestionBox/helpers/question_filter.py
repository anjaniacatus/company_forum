from faq.models import Question
from django.db.models import Q


def order_by_the_oldest_resolved_date():
    return Question.objects.order_by("resolved_date")


def order_by_the_recent_resolved_date():
    return Question.objects.order_by("-resolved_date")


def when_resolved_date_is_not_null():
    return Question.objects.filter(resolved_date__isnull=False)


def when_resolved_date_is_null():
    return Question.objects.filter(resolved_date__isnull=True)


def when_published_date_is_not_null_and_resolved_date_is__null():
    return Question.objects.filter(
        Q(published_date__isnull=False) and Q(resolved_date__isnull=True)
    )


def by_author_and_published_date_is_null(request):
    return Question.objects.filter(
        Q(author=request.user) and Q(published_date__isnull=False)
    )


def by_author_and_published_date_is_not_null(request):
    return Question.objects.filter(
        Q(author=request.user) and Q(published_date__isnull=True)
    )


def by_author_and_resolved_date_is_null(request):
    return Question.objects.filter(
        Q(author=request.user) and Q(resolved_date__isnull=True)
    )


def by_keywords(request):
    key_searched = request.POST["key_searched"]
    return Question.objects.filter(
        Q(title__contains=key_searched) | Q(answer__contains=key_searched)
    )

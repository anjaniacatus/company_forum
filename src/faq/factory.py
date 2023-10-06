import factory
from factory import fuzzy
from factory.faker import faker

from datetime import datetime, timezone

from django.contrib.auth.models import User
from .models import Question

FAKE = faker.Faker()


class ResolvedQuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    title = factory.Faker("sentence", nb_words=42)
    published_date = fuzzy.FuzzyDateTime(datetime(2023, 9, 26, tzinfo=timezone.utc))
    resolved_date = fuzzy.FuzzyDateTime(datetime(2023, 9, 26, tzinfo=timezone.utc))
    author = User.objects.get_or_create(username="Aina")[0]

    @factory.LazyAttribute
    def answer(self):
        content = ""
        for _ in range(0, 3):
            content += "\n" + FAKE.paragraph(nb_sentences=32) + "\n"
        return content


class UnresolvedQuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    title = factory.Faker("sentence", nb_words=42)
    published_date = fuzzy.FuzzyDateTime(datetime(2023, 9, 26, tzinfo=timezone.utc))
    resolved_date = None
    author = User.objects.get_or_create(username="Aina")[0]
    answer = ""


class DraftQuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    title = factory.Faker("sentence", nb_words=42)
    published_date = None
    resolved_date = None
    author = User.objects.get_or_create(username="Aina")[0]
    answer = "ceci est un test"


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    title = factory.Faker("sentence", nb_words=42)
    published_date = None
    resolved_date = None
    author = User.objects.get_or_create(username="Neo")

    @factory.LazyAttribute
    def answer(self):
        content = ""
        for _ in range(0, 3):
            content += "\n" + FAKE.paragraph(nb_sentences=32) + "\n"
        return content

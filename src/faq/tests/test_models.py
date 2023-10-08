from django.test import TestCase

import datetime

from faq.models import Question
from QuestionBox.helpers import question_filter
from faq.factory import *
from django.contrib.auth.models import User


class TestQuestion(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.get_or_create(username="Aina")

    def test_resolve(self):
        question = UnresolvedQuestionFactory.create()
        question.resolve()
        self.assertNotEqual(question.resolved_date, None)

    def test_publish(self):
        question = DraftQuestionFactory.create()
        question.publish()
        self.assertNotEqual(question.published_date, None)

    # unit test for QuestionBox.helpers
    def test_when_resolved_date_is_not_null(self):
        resolved_questions = ResolvedQuestionFactory.create_batch(3)
        filter_result = question_filter.when_resolved_date_is_not_null()
        self.assertEqual(len(filter_result), len(resolved_questions))

    def test_when_resolved_date_is_null(self):
        filter_result = question_filter.when_resolved_date_is_null()
        unresolved_questions = UnresolvedQuestionFactory.create_batch(2)
        self.assertEqual(len(filter_result), len(unresolved_questions))

    def test_when_published_date_is_not_null_and_resolved_date_is_null(self):
        filter_result = (
            question_filter.when_published_date_is_not_null_and_resolved_date_is_null()
        )
        published_questions = PublishedQuestionFactory.create_batch(2)
        self.assertEqual(len(filter_result), len(published_questions))

    def test_by_author_and_published_date_is_not_null(self):
        published_questions = PublishedQuestionFactory.create_batch(2)
        user = User.objects.get(username="Aina")
        filter_result = question_filter.by_author_and_published_date_is_not_null(user)
        print(filter_result)
        self.assertEqual(len(filter_result), len(published_questions))

    def test_by_author_and_published_date_is__null(self):
        unpublished_questions = UnpublishedQuestionFactory.create_batch(2)
        user = User.objects.get(username="Aina")
        filter_result = question_filter.by_author_and_published_date_is_null(user)
        print(filter_result)
        self.assertEqual(len(filter_result), len(unpublished_questions))

    def by_author_and_resolved_date_is_null(self):
        unresolved_questions = Question.objects.get(resolved_date__isnull=True)
        user = User.objects.get(username="Aina")
        filter_resulte = question_filter.by_author_and_resolved_date_is_nul(author)
        self.assertEqual(len(filter_result), len(unresolved_questions))

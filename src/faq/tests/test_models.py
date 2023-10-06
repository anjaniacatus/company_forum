from django.test import TestCase

import datetime
import pytest

from faq.models import Question
from faq.factory import UnresolvedQuestionFactory, DraftQuestionFactory
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestQuestion(TestCase):
    pytestmark = pytest.mark.django_db

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="Aina")

    def test_resolve(self):
        question = UnresolvedQuestionFactory.create()
        question.resolve()
        self.assertNotEqual(question.resolved_date, None)

    def test_publish(self):
        question = DraftQuestionFactory.create()
        question.publish()
        self.assertNotEqual(question.published_date, None)

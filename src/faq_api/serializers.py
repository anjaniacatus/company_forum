from rest_framework import serializers
from faq.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "id",
            "title",
            "answer",
            "author",
            "updated_at",
            "resolved_date",
            "published_date",
            "created_at",
        )

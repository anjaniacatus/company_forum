from faq.models import Question
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    endpoint that allows to get list of all responded questions

    """

    queryset = Question.objects.filter(resolved_date__isnull=False)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

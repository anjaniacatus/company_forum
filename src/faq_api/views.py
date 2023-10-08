from rest_framework import viewsets
from rest_framework import permissions
from .serializers import QuestionSerializer
from QuestionBox.helpers import question_filter


class QuestionViewSet(viewsets.ModelViewSet):
    """
    endpoint that allows to get list of all responded questions

    """

    queryset = question_filter.when_resolved_date_is_not_null()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

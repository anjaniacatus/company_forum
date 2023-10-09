from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from .serializers import QuestionSerializer
from QuestionBox.helpers import question_filter


class QuestionList(generics.ListAPIView):
    """
    endpoint that allows to get list of all responded questions

    """

    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = question_filter.when_resolved_date_is_not_null()

        username = self.request.query_params.get("username")
        if username is not None:
            author = User.objects.get(username=username)
            queryset = question_filter.by_author_and_published_date_is_not_null(author)
        return queryset

from rest_framework.viewsets import ModelViewSet

from stringfinder.api.serializers import TextSerializer
from stringfinder.models import Text


class TextViewSet(ModelViewSet):
    """
    TextViewSet contains necessary views for texts.
    """

    serializer_class = TextSerializer
    queryset = Text.objects.none()
    lookup_field = "id"

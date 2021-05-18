from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from stringfinder.api.serializers import TextSerializer
from stringfinder.models import Text


class TextViewSet(ModelViewSet):
    """
    TextViewSet contains necessary views for texts.
    """

    serializer_class = TextSerializer
    queryset = Text.objects.all()
    lookup_field = "id"

    @action(
        detail=False,
        methods=["post"],
        url_path="find-string",
        url_name="find-string-from-text",
        lookup_field="text",
    )
    def find_string(self, request):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            print(request.data["text"])
            if Text.objects.filter(text=request.data["text"]):
                return Response({"status": status.HTTP_200_OK})
            return Response({"status": status.HTTP_403_FORBIDDEN})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

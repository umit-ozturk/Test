from rest_framework import serializers

from stringfinder.models import Text


class TextSerializer(serializers.ModelSerializer):
    """
    TextSerializer
    """

    class Meta:
        model = Text
        fields = [
            "id",
            "text",
        ]
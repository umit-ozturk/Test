from django.utils.translation import gettext_lazy as _
from django.db import models


class Text(models.Model):
    """
    Text model contains the string.
    """

    text = models.TextField(
        _("Text"), null=True, blank=True
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("Text")
        verbose_name_plural = _("Texts")


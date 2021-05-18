from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StringFinderConfig(AppConfig):
    name = "stringfinder"
    verbose_name = _("String Finder")

    def ready(self):
        try:
            import stringfinder.signals  # noqa F401
        except ImportError:
            pass

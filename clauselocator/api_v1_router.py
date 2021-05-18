from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from stringfinder.api.views import TextViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("text", TextViewSet)

app_name = "api"

urlpatterns = router.urls

# urlpatterns = router.urls + [
#     path("", include("lorem.ipsum.dolor", namespace="lorem")),
# ]

from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet
from rest_framework import renderers


router = routers.DefaultRouter()
router.trailing_slash = "/?"

router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)

urlpatterns = (
    path('', include(router.urls)),
)
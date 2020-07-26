from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'api/items/', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include("api.project.urls")),
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # path("auth/", include("api.customAuth.urls")),
    # path("admin/", admin.site.urls),
    path("api/auth/", include("djoser.urls.authtoken")),
    path("auth/", include("djoser.urls")),
]

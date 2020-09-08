from django.urls import include, path
from rest_framework import routers
from .views import ItemViewSet, ItemLinkViewSet, WishListViewSet, AppGroupAdminViewSet

# from .views import FriendViewSet, BelongingViewSet, BorrowedViewSet

# from rest_framework import renderers


router = routers.DefaultRouter()
# router.trailing_slash = "/?"

router.register(r"item", ItemViewSet, basename="Item")
router.register(r"item_link", ItemLinkViewSet, basename="Itemlink")
router.register(r"wish_list", WishListViewSet, basename="WishList")
router.register(r"app_group_admin", AppGroupAdminViewSet, basename="AppGroupAdmin")

# router.register(r"friends", FriendViewSet)
# router.register(r"belongings", BelongingViewSet)
# router.register(r"borrowings", BorrowedViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

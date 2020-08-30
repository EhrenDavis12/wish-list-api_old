from django.urls import include, path
from rest_framework import routers
from .views import ItemViewSet, ItemLinkViewSet, WishListViewSet, GroupViewSet
# from .views import FriendViewSet, BelongingViewSet, BorrowedViewSet

# from rest_framework import renderers


router = routers.DefaultRouter()
# router.trailing_slash = "/?"

router.register(r"item", ItemViewSet, basename="Item")
router.register(r"item_link", ItemLinkViewSet, basename="Itemlink")
router.register(r"wish_list", WishListViewSet, basename="WishList")
router.register(r"Group", GroupViewSet, basename="Group")

# router.register(r"friends", FriendViewSet)
# router.register(r"belongings", BelongingViewSet)
# router.register(r"borrowings", BorrowedViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

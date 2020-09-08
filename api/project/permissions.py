from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Item, ItemLink


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


class IsOwner(permissions.BasePermission):
    message = "Not an owner."

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


class ItemPermission(BasePermission):
    def has_permission(self, request, view):
        try:
            pk = request.data.get("item")
            # pk = pk if pk else view.kwargs.get("pk")
            item = Item.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return False

        # return request.user.has_perm("item.is_owner", item)
        return item.owner == request.user


# class ItemLinkPermission(BasePermission):
#     def has_permission(self, request, view):
#         try:
#             link_pk =  view.kwargs.get("pk")
#             if link_pk is not None:
#                 item_link = ItemLink.objects.get(pk=link_pk).select_relat
#                 Item.objects.get()
#             Item

#             pk = pk if pk else request.data.get("item")
#             item = Item.objects.get(pk=pk)
#         except ObjectDoesNotExist:
#             return False

#         # return request.user.has_perm("item.is_owner", item)
#         return item.owner == request.user

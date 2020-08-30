from .models import Item, ItemLink, WishList, Group
# from .models import Friend, Belonging, Borrowed
from rest_framework import serializers

# from .permissions import IsOwnerOrReadOnly


class ItemLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemLink
        fields = ["id", "name", "link", "item"]


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    itemlinks = ItemLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ["id", "name", "is_purchased", "owner", "itemlinks"]


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ["id", "name"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name", "public_note"]


# class FriendSerializer(serializers.ModelSerializer):
#     owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

#     class Meta:
#         model = Friend
#         fields = ("id", "name", "has_overdue")


# class BelongingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Belonging
#         fields = ("id", "name")


# class BorrowedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Borrowed
#         fields = ("id", "what", "to_who", "when", "returned")

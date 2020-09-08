from .models import Item, ItemLink, WishList, AppGroup
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated

# from .permissions import IsOwnerOrReadOnly


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]
        read_only_fields = ["id", "username"]


class ItemLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemLink
        fields = ["id", "name", "link", "item"]
        read_only_fields = ["id", "item"]


class ItemLinkwriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemLink
        fields = ["id", "name", "link", "item"]
        read_only_fields = ["id"]

    def validate(self, data):
        item = data.get("item")
        if item.owner == self.context["request"].user:
            return data
        else:
            raise NotAuthenticated(detail=None, code=None)


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ["id", "name"]
        read_only_fields = ["id"]


class WishListWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ["id", "name"]
        read_only_fields = ["id"]


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    item_links = ItemLinkSerializer(many=True, read_only=True)
    wish_lists = WishListSerializer(source="wish_list", many=True)

    class Meta:
        model = Item
        # fields = "__all__"
        fields = [
            "id",
            "name",
            "is_purchased",
            "owner",
            "item_links",
            "wish_lists",
        ]


class ItemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "is_purchased",
            "owner",
            "wish_list",
        ]
        read_only_fields = ["id", "owner"]


class AppGroupSerializer(serializers.ModelSerializer):
    # member_list = serializers.ReadOnlyField(source="members")
    member_list = UserSerializer(many=True, read_only=True, source="members")

    class Meta:
        model = AppGroup
        fields = ["id", "name", "public_note", "member_list"]


class AppGroupWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppGroup
        fields = ["id", "name", "is_active"]
        read_only_fields = ["id"]

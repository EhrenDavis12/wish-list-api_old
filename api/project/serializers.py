from .models import Item, ItemLink
from .models import Friend, Belonging, Borrowed
from rest_framework import serializers

# from .permissions import IsOwnerOrReadOnly


class ItemLinkSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    # def validate(self, data):
    #     item = data.get('item', None)
    #     # try:
    #     #     item = Item.objects.get(pk=item_id)
    #     # except Item.DoesNotExist:
    #     #     raise serializers.ValidationError({"item": "Invalid id"})
    #     if not IsOwnerOrReadOnly().has_object_permission(request, None, item):
    #         raise serializers.ValidationError({"item": "Invalid id"})
    #     return data

    class Meta:
        model = ItemLink
        fields = ["id", "name", "link", "item"]


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    itemlinks = ItemLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ["id", "name", "is_purchased", "owner", "itemlinks"]


class FriendSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Friend
        fields = ("id", "name", "has_overdue")


class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Belonging
        fields = ("id", "name")


class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowed
        fields = ("id", "what", "to_who", "when", "returned")


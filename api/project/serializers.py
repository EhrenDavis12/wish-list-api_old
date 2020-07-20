from .models import Item, ItemLink
from rest_framework import serializers

class ItemLinkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def validate(self, data):
        item_id = data.get('item', None)
        if item_id is None:
            raise serializers.ValidationError({"item": "id is required"})
        return data

    class Meta:
        model = ItemLink
        fields = ['id', 'name', 'link', 'item']

class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    itemlinks = ItemLinkSerializer(many=True, read_only=True)
    class Meta:
        model = Item
        fields = ['id', 'name', 'is_purchased', 'owner', 'itemlinks']
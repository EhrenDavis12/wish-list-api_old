from django.contrib.auth.models import User, Group
from api.models import WishListItem, ItemLink
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']


class WishListItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WishListItem
        fields = ['id', 'name', 'is_purchased', 'user']


class ItemLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemLink
        fields = ['id', 'name', 'wish_list_item', 'link']

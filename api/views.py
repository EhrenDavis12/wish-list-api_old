from django.contrib.auth.models import User, Group
from api.models import WishListItem, ItemLink
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, WishListItemSerializer, ItemLinkSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # http_method_names = ['get', 'patch', 'post']


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # http_method_names = ['get', 'patch', 'post']


class WishListItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows WishListItem to be viewed or edited.
    """
    queryset = WishListItem.objects.all()
    serializer_class = WishListItemSerializer
    # http_method_names = ['get', 'patch', 'post']


class ItemLinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ItemLink to be viewed or edited.
    """
    queryset = ItemLink.objects.all()
    serializer_class = ItemLinkSerializer
    # http_method_names = ['get', 'patch', 'post']

# from django.contrib.auth.models import User
from .models import Item, ItemLink, WishList, Group
# from .models import Friend, Belonging, Borrowed
from rest_framework import viewsets
from .serializers import ItemSerializer, ItemLinkSerializer, WishListSerializer, GroupSerializer
# from .serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly, IsOwner
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        # this seems in-efficient
        items = self.queryset.filter(owner=self.request.user)
        item = get_object_or_404(items, pk=pk)
        return item

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, request, pk=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def list(self, request):
        items = self.queryset.filter(owner=self.request.user)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "success", "data": "invalid data"})


class ItemLinkViewSet(viewsets.ModelViewSet):
    queryset = ItemLink.objects.all()
    serializer_class = ItemLinkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"status": "success", "pk": serializer.instance.pk})

    def list(self, request):
        return Response({"status": "error", "data": "Use Items to get list of links"})


class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"status": "success", "pk": serializer.instance.pk})


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"status": "success", "pk": serializer.instance.pk})


# class FriendViewSet(viewsets.ModelViewSet):
#     # queryset = Friend.objects.all()
#     queryset = Friend.objects.with_overdue()
#     serializer_class = FriendSerializer
#     permission_classes = [IsOwner]


# class BelongingViewSet(viewsets.ModelViewSet):
#     queryset = Belonging.objects.all()
#     serializer_class = BelongingSerializer


# class BorrowedViewSet(viewsets.ModelViewSet):
#     queryset = Borrowed.objects.all()
#     serializer_class = BorrowedSerializer

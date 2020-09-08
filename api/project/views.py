from .models import Item, ItemLink, WishList, AppGroup
from rest_framework import viewsets
from .serializers import (
    ItemSerializer,
    ItemWriteSerializer,
    ItemLinkSerializer,
    ItemLinkwriteSerializer,
    WishListSerializer,
    WishListWriteSerializer,
    AppGroupSerializer,
    AppGroupWriteSerializer,
)
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly, IsOwner, ItemPermission
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(owner=self.request.user)

    def get_object(self, pk):
        items = self.get_queryset()
        item = get_object_or_404(items, pk=pk)
        return item

    def create(self, request, *args, **kwargs):
        serializer = ItemWriteSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user)
        return Response({"status": "success", "pk": serializer.instance.pk})

    def retrieve(self, request, pk=None):
        item = self.get_object(pk)
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def list(self, request):
        items = self.get_queryset()
        serializer = self.get_serializer(items, many=True)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        item = self.get_object(pk)
        # serializer = self.get_serializer(item, data=request.data, partial=True)
        serializer = ItemWriteSerializer(
            item, data=request.data, context={"request": request}, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "Error", "data": "invalid data"})


class ItemLinkViewSet(viewsets.ModelViewSet):
    queryset = ItemLink.objects.all()
    serializer_class = ItemLinkSerializer
    permission_classes = [IsAuthenticated]  # , ItemPermission]

    def get_object(self, pk):
        item_links = self.queryset.filter(item__owner=self.request.user)
        item_link = get_object_or_404(item_links, pk=pk)
        return item_link

    def create(self, request, *args, **kwargs):
        serializer = ItemLinkwriteSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": "success", "pk": serializer.instance.pk})

    def list(self, request):
        return Response({"status": "error", "data": "Use Items to get list of links"})

    def retrieve(self, request, pk=None):
        item_link = self.get_object(pk)
        serializer = ItemLinkSerializer(item_link)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        item_link = self.get_object(pk)
        serializer = ItemLinkSerializer(item_link, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "Error", "data": "invalid data"})

    def destroy(self, request, pk=None):
        item_link = self.get_object(pk)
        item_link.delete()
        return Response({"status": "success", "data": "Item Link has been deleted"})


class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WishList.objects.filter(owner=self.request.user)

    def get_object(self, pk):
        wish_lists = self.get_queryset()
        wish_list = get_object_or_404(wish_lists, pk=pk)
        return wish_list

    def create(self, request, *args, **kwargs):
        serializer = WishListWriteSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user)
        return Response({"status": "success", "pk": serializer.instance.pk})

    def list(self, request):
        wish_lists = self.get_queryset()
        serializer = self.get_serializer(wish_lists, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        wish_list = self.get_object(pk)
        serializer = self.get_serializer(wish_list)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        wish_list = self.get_object(pk)
        serializer = self.get_serializer(wish_list, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "Error", "data": "invalid data"})

    def destroy(self, request, pk=None):
        wish_list = self.get_object(pk)
        wish_list.delete()
        return Response({"status": "success", "data": "Wish list has been deleted"})


class AppGroupAdminViewSet(viewsets.ModelViewSet):
    queryset = AppGroup.objects.all()
    serializer_class = AppGroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return AppGroup.objects.filter(owner=self.request.user)

    def get_object(self, pk):
        app_groups = self.get_queryset()
        app_group = get_object_or_404(app_groups, pk=pk)
        return app_group

    def create(self, request, *args, **kwargs):
        serializer = AppGroupWriteSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user, members=[request.user])
        return Response({"status": "success", "pk": serializer.instance.pk})

    def list(self, request):
        app_groups = self.get_queryset()
        serializer = self.get_serializer(app_groups, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        app_group = self.get_object(pk)
        serializer = self.get_serializer(app_group)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        app_group = self.get_object(pk)
        serializer = self.get_serializer(app_group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "Error", "data": "invalid data"})

    def destroy(self, request, pk=None):
        app_group = self.get_object(pk)
        app_group.delete()
        return Response({"status": "success", "data": "AppGroup has been deleted"})

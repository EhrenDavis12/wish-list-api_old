# from django.contrib.auth.models import User
from .models import Item, ItemLink
from .models import Friend, Belonging, Borrowed
from rest_framework import viewsets
from .serializers import ItemSerializer, ItemLinkSerializer
from .serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly, IsOwner
from rest_framework.response import Response

# Create your views here.


class ItemViewSet(viewsets.ModelViewSet):
    # """
    # API endpoint that allows Item to be viewed or edited.
    # """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # def create(self, *args, **kwargs):
        #     super(Item, self).save(*args, **kwargs)


class ItemLinkViewSet(viewsets.ModelViewSet):
    # """
    # API endpoint that allows ItemLink to be viewed or edited.
    # """
    queryset = ItemLink.objects.all()
    serializer_class = ItemLinkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"status": "success", "pk": serializer.instance.pk})


class FriendViewSet(viewsets.ModelViewSet):
    # queryset = Friend.objects.all()
    queryset = Friend.objects.with_overdue()
    serializer_class = FriendSerializer
    permission_classes = [IsOwner]


class BelongingViewSet(viewsets.ModelViewSet):
    queryset = Belonging.objects.all()
    serializer_class = BelongingSerializer


class BorrowedViewSet(viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer

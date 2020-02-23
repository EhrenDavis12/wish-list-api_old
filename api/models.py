import uuid
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class WishListItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    is_purchased = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ItemLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    wish_list_item = models.ForeignKey(WishListItem, on_delete=models.CASCADE)
    link = models.TextField()

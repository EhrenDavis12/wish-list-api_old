import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    is_purchased = models.BooleanField()
    owner = models.ForeignKey(User, related_name='wish_list_item', on_delete=models.CASCADE)
    created = models.DateTimeField(default=now, editable=False)

    def save(self, *args, **kwargs):
        super(Item, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created']


class ItemLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(
        Item,
        related_name='itemlinks',
        default='1538900e-97b7-4567-83f3-7565c0b8f604',
        on_delete=models.CASCADE
    )
    name = models.TextField()
    link = models.TextField()
    created = models.DateTimeField(default=now, editable=False)

    class Meta:
        ordering = ['created']

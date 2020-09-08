import uuid
from django.db import models
from django.contrib.auth.models import User
import pendulum


class BassModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(default=pendulum.now, editable=False)
    lastUpdated = models.DateTimeField(default=pendulum.now, editable=True)

    class Meta:
        ordering = ["created"]
        abstract = True


class OwnedModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class AppGroup(BassModel, OwnedModel):
    members = models.ManyToManyField(User, related_name="group_member")
    # admin_members = models.ManyToManyField(User, related_name="group_admin_member")
    name = models.TextField(blank=True, null=False, default="")
    public_note = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(null=False, default=True)
    # deactivate_after = models.DateField(blank=True, null=True, editable=True)


class WishList(BassModel, OwnedModel):
    groups = models.ManyToManyField(AppGroup, related_name="groups")
    name = models.TextField(blank=True, null=False, default="")
    public_note = models.TextField(blank=True, null=True)
    private_note = models.TextField(blank=True, null=True)


class Item(BassModel, OwnedModel):
    name = models.TextField()
    wish_list = models.ManyToManyField(WishList, related_name="wish_lists")
    is_purchased = models.BooleanField(null=False, default=True)


class ItemLink(BassModel):
    item = models.ForeignKey(Item, related_name="item_links", on_delete=models.CASCADE)
    name = models.TextField(blank=True, null=False, default="")
    link = models.TextField(blank=True, null=False, default="")
    description = models.TextField(blank=True, null=True)

import uuid
from django.db import models
from django.contrib.auth.models import User
# from .manager import FriendQuerySet
import pendulum

# from django.conf import settings

# Create your models here.


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


class Group(BassModel, OwnedModel):
    members = models.ManyToManyField(User, related_name="group_member")
    admin_members = models.ManyToManyField(
        User, related_name="group_admin_member")
    name = models.TextField()
    public_note = models.TextField()
    # is_active = models.BooleanField()
    # deactivate_after = models.DateField()


class WishList(BassModel, OwnedModel):
    groups = models.ManyToManyField(Group)
    name = models.TextField()
    public_note = models.TextField()
    private_note = models.TextField()


class Item(BassModel, OwnedModel):
    name = models.TextField()
    wish_list = models.ManyToManyField(WishList)
    is_purchased = models.BooleanField()

    def save(self, *args, **kwargs):
        super(Item, self).save(*args, **kwargs)


class ItemLink(BassModel):
    item = models.ForeignKey(
        Item,
        related_name="itemlinks",
        # default="1538900e-97b7-4567-83f3-7565c0b8f604",
        on_delete=models.CASCADE,
    )
    name = models.TextField()
    link = models.TextField()
    description = models.TextField()


# class Friend(models.Model):
#     name = models.CharField(max_length=100)

#     objects = FriendQuerySet.as_manager()

#     @property
#     def has_overdue(self):
#         if hasattr(self, "ann_overdue"):  # in case we deal with annotated object
#             return self.ann_overdue
#         return self.borrowed_set.filter(  # 1
#             returned__isnull=True, when=pendulum.now.subtract(months=2)
#         ).exists()


# class Belonging(OwnedModel):
#     name = models.CharField(max_length=100)


# class Borrowed(models.Model):
#     what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
#     to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
#     when = models.DateTimeField(auto_now_add=True)
#     returned = models.DateTimeField(default=None, null=True, blank=True)

# Generated by Django 3.0.2 on 2020-08-29 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pendulum
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=pendulum.now, editable=False)),
                ('lastUpdated', models.DateTimeField(default=pendulum.now)),
                ('name', models.TextField()),
                ('public_note', models.TextField()),
                ('admin_members', models.ManyToManyField(related_name='group_admin_member', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='group_member', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=pendulum.now, editable=False)),
                ('lastUpdated', models.DateTimeField(default=pendulum.now)),
                ('name', models.TextField()),
                ('public_note', models.TextField()),
                ('private_note', models.TextField()),
                ('groups', models.ManyToManyField(to='project.Group')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='item',
            name='wish_list',
            field=models.ManyToManyField(to='project.WishList'),
        ),
    ]
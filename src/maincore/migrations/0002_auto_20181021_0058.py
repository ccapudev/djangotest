# Generated by Django 2.1 on 2018-10-21 00:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('maincore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='field',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='model',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='setting',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
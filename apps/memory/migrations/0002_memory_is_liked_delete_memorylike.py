# Generated by Django 4.2.13 on 2024-06-04 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memory',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='MemoryLike',
        ),
    ]

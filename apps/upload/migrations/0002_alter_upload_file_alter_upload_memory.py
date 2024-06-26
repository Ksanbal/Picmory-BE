# Generated by Django 4.2.13 on 2024-06-04 14:30

import apps.upload.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0002_memory_is_liked_delete_memorylike'),
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(max_length=255, upload_to=apps.upload.models.upload_to),
        ),
        migrations.AlterField(
            model_name='upload',
            name='memory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='uploads', to='memory.memory'),
        ),
    ]

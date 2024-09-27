# Generated by Django 3.2.8 on 2021-11-11 02:37

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0004_resource_polymorphic_ctype"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="resource",
            managers=[
                ("templates", django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name="resource",
            name="polymorphic_ctype",
        ),
    ]

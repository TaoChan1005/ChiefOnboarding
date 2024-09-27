# Generated by Django 3.2.8 on 2021-10-23 02:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin_tasks", "0003_auto_20211023_0204"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admintask",
            name="email",
            field=models.EmailField(blank=True, default="", max_length=12500),
        ),
        migrations.AlterField(
            model_name="admintask",
            name="slack_user",
            field=models.CharField(blank=True, default="", max_length=12500),
        ),
    ]

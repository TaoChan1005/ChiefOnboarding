# Generated by Django 4.2.6 on 2023-10-24 22:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("integrations", "0021_alter_integration_manifest_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="integration",
            name="manifest",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name="integration",
            name="manifest_type",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (0, "Provision user accounts or trigger webhooks"),
                    (1, "Sync users"),
                    (3, "Manual user account provisioning, no manifest required"),
                ],
                null=True,
            ),
        ),
    ]

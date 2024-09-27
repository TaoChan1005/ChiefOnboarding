# Generated by Django 3.2.10 on 2022-01-17 22:26

from django.db import migrations, models

from misc.migration_scripts.content_migrations import (
    RunPythonWithArguments,
    migrate_wysiwyg_field,
)


class Migration(migrations.Migration):
    dependencies = [
        ("badges", "0003_remove_badge_polymorphic_ctype"),
    ]

    operations = [
        migrations.AddField(
            model_name="badge",
            name="content_json",
            field=models.JSONField(default=dict),
        ),
        RunPythonWithArguments(
            migrate_wysiwyg_field, context={"app": "badges", "model": "badge"}
        ),
    ]

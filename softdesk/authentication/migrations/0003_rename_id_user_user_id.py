# Generated by Django 5.0.4 on 2024-04-11 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_contributor_project"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="id",
            new_name="user_id",
        ),
    ]
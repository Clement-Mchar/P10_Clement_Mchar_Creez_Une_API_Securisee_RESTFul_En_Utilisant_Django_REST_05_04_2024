# Generated by Django 5.0.4 on 2024-04-12 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0005_issue_priority_issue_tag_alter_project_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issue",
            name="priority",
            field=models.CharField(
                choices=[("LOW", "low"), ("MEDIUM", "medium"), ("HIGH", "high")],
                default="putain mais nique ta grand mère",
                max_length=15,
            ),
        ),
    ]
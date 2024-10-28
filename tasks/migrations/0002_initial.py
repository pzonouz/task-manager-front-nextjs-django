# Generated by Django 5.1.2 on 2024-10-28 06:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("priorities", "0001_initial"),
        ("projects", "0001_initial"),
        ("tags", "0001_initial"),
        ("tasks", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="priority",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="tasks",
                to="priorities.priority",
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="projects.project",
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="tags",
            field=models.ManyToManyField(related_name="tasks", to="tags.tag"),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-08 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_projectnotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectnotes',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='projects.project'),
            preserve_default=False,
        ),
    ]

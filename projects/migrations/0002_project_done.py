# Generated by Django 5.0.4 on 2024-05-06 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]

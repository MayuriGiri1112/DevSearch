# Generated by Django 5.0.4 on 2024-04-14 21:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_options'),
        ('users', '0005_alter_profile_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]

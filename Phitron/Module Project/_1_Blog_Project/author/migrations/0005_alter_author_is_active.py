# Generated by Django 5.1.2 on 2024-11-04 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0004_author_created_at_author_is_active_author_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

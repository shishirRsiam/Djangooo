# Generated by Django 5.1.2 on 2024-11-29 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library_App', '0002_borrow'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=1),
            preserve_default=1,
        ),
    ]
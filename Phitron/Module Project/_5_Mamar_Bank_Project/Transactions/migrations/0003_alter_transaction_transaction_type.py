# Generated by Django 5.1.2 on 2024-11-20 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0002_rename_account_transaction_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(max_length=50),
        ),
    ]
# Generated by Django 5.1.2 on 2024-11-09 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_alter_task_taskdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='taskAssignDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

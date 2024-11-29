# Generated by Django 5.1.2 on 2024-11-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='Library_App/categories')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=500)),
                ('description', models.TextField(null=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('available_copies', models.IntegerField(default=1)),
                ('img', models.ImageField(upload_to='Library_App/books')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='Library_App.categorie')),
            ],
        ),
    ]

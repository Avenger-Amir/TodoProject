# Generated by Django 3.2.11 on 2022-01-30 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUserForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
            ],
        ),
    ]

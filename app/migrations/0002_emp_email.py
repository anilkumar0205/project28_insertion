# Generated by Django 4.2.6 on 2023-12-11 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='email',
            field=models.CharField(default='employe@gmail.com', max_length=100),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice_api', '0005_alter_welcome_greetings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welcome',
            name='greetings',
            field=models.CharField(default='Good  morning!', max_length=100),
        ),
    ]

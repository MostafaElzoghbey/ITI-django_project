# Generated by Django 4.2.5 on 2023-09-21 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authmansoura', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myaccount',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
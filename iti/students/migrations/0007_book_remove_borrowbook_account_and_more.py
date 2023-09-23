# Generated by Django 4.2.5 on 2023-09-23 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authmansoura', '0003_alter_myaccount_is_admin'),
        ('students', '0006_alter_borrowbook_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=150)),
                ('is_borrowed', models.BooleanField(default=False)),
                ('returnTime', models.DateTimeField(null=True)),
                ('photoName', models.CharField(default='1.jpg', max_length=50)),
                ('borrowed_by_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authmansoura.myaccount')),
            ],
        ),
        migrations.RemoveField(
            model_name='borrowbook',
            name='account',
        ),
        migrations.RemoveField(
            model_name='borrowbook',
            name='borrbook',
        ),
        migrations.DeleteModel(
            name='books',
        ),
        migrations.DeleteModel(
            name='borrowbook',
        ),
    ]

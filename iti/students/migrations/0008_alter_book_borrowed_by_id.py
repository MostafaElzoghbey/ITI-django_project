# Generated by Django 4.2.5 on 2023-09-23 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authmansoura', '0003_alter_myaccount_is_admin'),
        ('students', '0007_book_remove_borrowbook_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrowed_by_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authmansoura.myaccount'),
        ),
    ]

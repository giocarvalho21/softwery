# Generated by Django 3.1.4 on 2020-12-31 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_id_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id_company',
            new_name='company',
        ),
    ]

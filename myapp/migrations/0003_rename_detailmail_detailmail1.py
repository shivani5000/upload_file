# Generated by Django 4.1.4 on 2023-01-06 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_email_detailmail_email1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='detailmail',
            new_name='detailmail1',
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-08 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pub_date',
            new_name='publish_date',
        ),
    ]
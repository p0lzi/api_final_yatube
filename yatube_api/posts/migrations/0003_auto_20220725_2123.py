# Generated by Django 2.2.16 on 2022-07-25 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220725_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
    ]
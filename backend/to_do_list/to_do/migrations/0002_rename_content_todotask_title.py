# Generated by Django 4.0.4 on 2022-04-12 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todotask',
            old_name='content',
            new_name='title',
        ),
    ]
# Generated by Django 5.1.6 on 2025-02-15 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passwordreset',
            old_name='token',
            new_name='token_pass',
        ),
    ]

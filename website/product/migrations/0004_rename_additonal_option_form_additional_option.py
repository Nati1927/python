# Generated by Django 5.0.1 on 2024-02-29 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_form'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='additonal_option',
            new_name='additional_option',
        ),
    ]

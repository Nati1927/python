# Generated by Django 5.0.1 on 2024-02-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_img_home_background_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('car_brand', models.CharField(max_length=100)),
                ('car_model', models.CharField(max_length=100)),
                ('additonal_option', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
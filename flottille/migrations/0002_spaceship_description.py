# Generated by Django 4.1.7 on 2023-03-03 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flottille', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spaceship',
            name='description',
            field=models.TextField(default='-', max_length=400),
            preserve_default=False,
        ),
    ]

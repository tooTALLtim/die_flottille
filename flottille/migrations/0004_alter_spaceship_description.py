# Generated by Django 4.1.7 on 2023-03-03 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flottille', '0003_alter_spaceship_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spaceship',
            name='description',
            field=models.TextField(),
        ),
    ]

# Generated by Django 4.0.5 on 2022-09-29 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0005_remove_apartment_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

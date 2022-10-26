# Generated by Django 4.0.5 on 2022-09-27 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('num_bathrooms', models.FloatField()),
                ('num_bedrooms', models.IntegerField()),
                ('square_footage', models.IntegerField()),
                ('adress', models.CharField(max_length=100)),
            ],
        ),
    ]

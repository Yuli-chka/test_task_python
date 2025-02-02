# Generated by Django 5.1.2 on 2024-10-16 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streets', to='my_app.city')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('house', models.CharField(max_length=10)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.city')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.street')),
            ],
        ),
    ]

# Generated by Django 3.2 on 2022-06-21 19:49

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MtaaniDeals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetterRecepients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOfPeople', models.IntegerField()),
                ('date', models.DateField(unique=True)),
                ('time', models.TimeField(unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('photo', cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/fevercode/image/upload/v1654534329/default_n0r7rf.png', max_length=255, verbose_name='image')),
                ('name', models.CharField(max_length=255)),
                ('Tel', models.IntegerField(null=True, unique=True)),
                ('location', models.CharField(max_length=255)),
                ('reservation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.reservation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

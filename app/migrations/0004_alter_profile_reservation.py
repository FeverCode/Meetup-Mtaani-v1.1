# Generated by Django 3.2 on 2022-06-21 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_profile_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='reservation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.reservation'),
        ),
    ]

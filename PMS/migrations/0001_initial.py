# Generated by Django 3.1.8 on 2021-04-06 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=100, unique=True)),
                ('national_id_number', models.CharField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('district', models.CharField(max_length=100)),
                ('date_of_birth', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
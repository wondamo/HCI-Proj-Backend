# Generated by Django 4.1.5 on 2023-01-16 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email Address')),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('resource_id', models.CharField(max_length=35, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=25)),
                ('reg_no', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_date', models.DateField()),
                ('return_date', models.DateField()),
                ('returned', models.BooleanField(default=False)),
                ('expired', models.BooleanField(default=False)),
                ('resource', models.ManyToManyField(to='staff.resource')),
                ('student', models.ManyToManyField(to='staff.student')),
            ],
        ),
    ]

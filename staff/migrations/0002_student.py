# Generated by Django 4.1.5 on 2023-01-16 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
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
    ]

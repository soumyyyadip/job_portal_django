# Generated by Django 3.2.16 on 2023-06-08 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0016_alter_job_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=120)),
                ('phone', models.IntegerField(max_length=120)),
                ('message', models.CharField(max_length=120)),
            ],
        ),
    ]
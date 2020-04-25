# Generated by Django 3.0.4 on 2020-04-22 07:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('img', models.ImageField(upload_to='pics')),
                ('post_desc', models.TextField(default='')),
            ],
        ),
    ]
# Generated by Django 2.2.2 on 2019-07-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='untitled')),
                ('photo', models.ImageField(upload_to='%y%m%d')),
                ('author', models.TextField(default='anonymous')),
            ],
        ),
    ]
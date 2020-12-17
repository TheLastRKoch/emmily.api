# Generated by Django 3.1.4 on 2020-12-15 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('phonetic', models.CharField(max_length=100)),
                ('definition', models.TextField(blank=True, max_length=100)),
                ('example', models.TextField(blank=True, max_length=100)),
            ],
        ),
    ]
# Generated by Django 3.1.4 on 2020-12-23 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordlist_skill', '0005_word_urban_definition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='phonetic',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

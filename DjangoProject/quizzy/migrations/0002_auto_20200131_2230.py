# Generated by Django 3.0.2 on 2020-01-31 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='addresses',
        ),
        migrations.RemoveField(
            model_name='person',
            name='birth_date',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]

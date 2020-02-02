# Generated by Django 3.0.2 on 2020-01-31 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, max_length=450, null=True)),
                ('addresses', models.ManyToManyField(related_name='persons', to='quizzy.Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

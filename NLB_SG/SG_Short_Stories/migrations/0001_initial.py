# Generated by Django 3.0.1 on 2019-12-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('language', models.CharField(blank=True, max_length=30)),
                ('summary', models.TextField()),
                ('publish_year', models.DateField()),
                ('download_link', models.URLField()),
            ],
        ),
    ]

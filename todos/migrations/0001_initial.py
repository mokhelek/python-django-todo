# Generated by Django 4.1.6 on 2023-02-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]

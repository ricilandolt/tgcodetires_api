# Generated by Django 4.2.9 on 2024-01-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rimdimenesion', models.CharField(max_length=20)),
            ],
        ),
    ]

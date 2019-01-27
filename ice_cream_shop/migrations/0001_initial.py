# Generated by Django 2.1.5 on 2019-01-25 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(max_length=100)),
                ('base', models.CharField(max_length=100)),
                ('available', models.CharField(max_length=100)),
                ('featured', models.CharField(max_length=100)),
                ('churned', models.DateField()),
            ],
        ),
    ]

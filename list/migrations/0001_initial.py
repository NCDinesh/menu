# Generated by Django 4.2 on 2023-07-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=100)),
                ('itemid', models.IntegerField()),
                ('itemtype', models.CharField(max_length=50)),
                ('itemprice', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2023-01-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0003_test_field4'),
    ]

    operations = [
        migrations.CreateModel(
            name='mesta',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('spektakl', models.CharField(max_length=50)),
                ('sektor', models.CharField(max_length=50)),
                ('mesto', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=50)),
                ('sms', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='spektakl',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('nazvanie', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]

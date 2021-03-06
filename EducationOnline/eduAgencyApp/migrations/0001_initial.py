# Generated by Django 2.1 on 2019-06-17 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyForm_a',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('field', models.CharField(max_length=100)),
                ('idcode', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='ApplyForm_t',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=1)),
                ('age', models.PositiveSmallIntegerField()),
            ],
        ),
    ]

# Generated by Django 2.2.2 on 2019-06-19 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('privilege', models.PositiveSmallIntegerField()),
                ('audited', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='parents.Users')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=4)),
                ('balance', models.PositiveIntegerField(default=0)),
                ('child_name', models.CharField(max_length=10)),
                ('child_age', models.IntegerField(default=10)),
                ('child_sex', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starts', models.PositiveSmallIntegerField(default=5)),
                ('words', models.CharField(max_length=50)),
                ('images', models.ImageField(upload_to='img')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parents.Users')),
            ],
        ),
    ]
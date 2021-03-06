# Generated by Django 3.1 on 2020-10-03 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField(help_text='Enter a brief desc of academy', max_length=1000)),
                ('address', models.TextField(help_text='Enter address of academy', max_length=1000)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sports_name', models.CharField(max_length=200)),
                ('sports_type', models.CharField(max_length=200)),
                ('academy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sports.academy')),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('exp', models.IntegerField()),
                ('academy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sports.academy')),
            ],
        ),
    ]

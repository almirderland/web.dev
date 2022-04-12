# Generated by Django 4.0.4 on 2022-04-12 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('count', models.IntegerField()),
                ('is_active', models.BooleanField()),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
        ),
    ]

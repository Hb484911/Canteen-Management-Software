# Generated by Django 3.2.5 on 2022-05-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteenapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobileno', models.CharField(max_length=12)),
                ('fooditem', models.CharField(max_length=20)),
                ('quantity', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
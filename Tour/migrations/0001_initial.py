# Generated by Django 3.2.9 on 2021-11-17 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
                ('desc', models.CharField(default='', max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Destination_name', models.CharField(max_length=100)),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(default='0', upload_to='images')),
                ('desc', models.CharField(max_length=6000)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]

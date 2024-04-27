# Generated by Django 5.0.4 on 2024-04-20 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=100)),
                ('stu_email', models.EmailField(max_length=254)),
                ('stu_city', models.CharField(max_length=100)),
                ('stu_mobile', models.IntegerField()),
            ],
        ),
    ]

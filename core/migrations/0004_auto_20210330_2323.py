# Generated by Django 3.1.7 on 2021-03-30 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_host_last_sub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='username',
            field=models.CharField(blank=True, default='null', max_length=50),
        ),
    ]
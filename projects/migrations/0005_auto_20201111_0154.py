# Generated by Django 3.1.3 on 2020-11-10 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20201110_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]

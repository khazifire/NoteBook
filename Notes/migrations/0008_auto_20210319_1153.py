# Generated by Django 3.1.7 on 2021-03-19 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0007_auto_20210319_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='update_date',
            field=models.DateTimeField(default=models.DateTimeField(auto_now_add=True, verbose_name='Date Created'), verbose_name='Date Modified'),
        ),
    ]
# Generated by Django 2.1.5 on 2019-02-18 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mon_app', '0010_auto_20190218_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='groupId',
            field=models.SlugField(blank=True, max_length=300, null=True, verbose_name='ID группы'),
        ),
    ]
# Generated by Django 2.1.5 on 2019-02-22 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mon_app', '0032_remove_match_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='name_my',
            field=models.CharField(blank=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', max_length=300, null=True, verbose_name='Товар'),
        ),
    ]
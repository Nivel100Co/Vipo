# Generated by Django 2.0.7 on 2018-08-10 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coproperties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='Letter',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Block'),
        ),
        migrations.AddField(
            model_name='property',
            name='Number',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='House/Apartment'),
        ),
        migrations.AlterField(
            model_name='property',
            name='Code',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Code'),
        ),
    ]

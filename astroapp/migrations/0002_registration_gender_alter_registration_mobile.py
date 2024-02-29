# Generated by Django 4.2.6 on 2023-10-14 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astroapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], default=52, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]

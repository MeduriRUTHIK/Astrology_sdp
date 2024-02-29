# Generated by Django 4.2.6 on 2023-10-14 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astroapp', '0002_registration_gender_alter_registration_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('email', models.EmailField(max_length=254)),
                ('rating', models.CharField(choices=[('outstanding', 'Outstanding'), ('good', 'Good'), ('ok', 'Ok'), ('bad', 'Bad')], max_length=30)),
                ('suggestions', models.TextField()),
            ],
            options={
                'db_table': 'Feedback',
            },
        ),
    ]

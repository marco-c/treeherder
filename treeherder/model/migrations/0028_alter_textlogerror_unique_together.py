# Generated by Django 3.2.13 on 2022-06-27 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0027_mozciclassification'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='textlogerror',
            unique_together={('step', 'line_number'), ('job', 'line_number')},
        ),
    ]

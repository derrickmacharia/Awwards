# Generated by Django 3.2.9 on 2021-12-13 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwardsApp', '0004_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='avg_rate',
            new_name='average',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='content_rate',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='design_rate',
            new_name='design',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='usability_rate',
            new_name='usability',
        ),
    ]

# Generated by Django 3.0 on 2021-07-27 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_auto_20210726_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='create_date',
            field=models.DateField(auto_now=True),
        ),
    ]

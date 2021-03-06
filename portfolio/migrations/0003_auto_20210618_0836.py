# Generated by Django 3.0 on 2021-06-18 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='initial_investment_amount',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolio',
            name='investment_horizon',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]

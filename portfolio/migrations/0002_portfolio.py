# Generated by Django 3.0 on 2021-06-18 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type_investor', models.PositiveSmallIntegerField(choices=[(0, 'qualified_investor'), (1, 'unqualified_investor')])),
                ('currency', models.PositiveSmallIntegerField(choices=[(0, 'dollars'), (1, 'rubles')])),
                ('maximum_allowable_drawdown', models.PositiveIntegerField()),
                ('type_according_risk_reward', models.PositiveSmallIntegerField(choices=[(0, 'aggressive'), (1, 'conservative'), (2, 'balanced')])),
                ('focus', models.PositiveSmallIntegerField(choices=[(0, 'minimum_loss'), (1, 'maximum_profit')])),
                ('types_assets', models.PositiveSmallIntegerField(choices=[(0, 'shares_of_Russian_companies'), (1, 'international_promotions'), (2, 'commodity_markets')])),
                ('ETF', models.PositiveSmallIntegerField(choices=[(0, 'yes'), (1, 'no'), (2, 'exclusively_in_etf')])),
            ],
        ),
    ]

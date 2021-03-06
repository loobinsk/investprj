# Generated by Django 3.0 on 2021-06-18 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210618_0836'),
        ('portfolio', '0003_auto_20210618_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='investmen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.InvestmentAdvisor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='currency',
            field=models.PositiveSmallIntegerField(choices=[(0, 'dollars'), (1, 'rubles')], verbose_name='валюта'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='focus',
            field=models.PositiveSmallIntegerField(choices=[(0, 'minimum_loss'), (1, 'maximum_profit')], verbose_name='фокус'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='initial_investment_amount',
            field=models.PositiveIntegerField(verbose_name='начальная сумма инвестиций'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='investment_horizon',
            field=models.PositiveIntegerField(verbose_name='инвестиционный горизонт'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='maximum_allowable_drawdown',
            field=models.PositiveIntegerField(verbose_name='максимально допустимая просадка'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='name',
            field=models.CharField(max_length=255, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='type_according_risk_reward',
            field=models.PositiveSmallIntegerField(choices=[(0, 'aggressive'), (1, 'conservative'), (2, 'balanced')], verbose_name='тип по соотношению риска/прибыли'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='type_investor',
            field=models.PositiveSmallIntegerField(choices=[(0, 'qualified_investor'), (1, 'unqualified_investor')], verbose_name='тип инвестора'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='types_assets',
            field=models.PositiveSmallIntegerField(choices=[(0, 'shares_of_Russian_companies'), (1, 'international_promotions'), (2, 'commodity_markets')], verbose_name='тип акций'),
        ),
    ]

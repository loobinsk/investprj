# Generated by Django 3.0 on 2021-08-12 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0027_portfolio_shares_blacklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='ETF',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Да'), (1, 'Нет'), (2, 'Только в ETF')]),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='active',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='currency',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Доллары'), (1, 'Рубли')], verbose_name='валюта'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='focus',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Минимальные просадки'), (1, 'Максимальная прибыль')], verbose_name='фокус'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='initial_investment_amount',
            field=models.PositiveIntegerField(blank=True, verbose_name='начальная сумма инвестиций'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='investment_horizon',
            field=models.PositiveIntegerField(blank=True, verbose_name='инвестиционный горизонт'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='investment_strategy',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'по умолчанию'), (1, 'Фокус на рост'), (2, 'Фокус на диверсификацию')], verbose_name='инвестиционная стратегия'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='maximum_allowable_drawdown',
            field=models.FloatField(blank=True, verbose_name='максимально допустимая просадка'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='type_according_risk_reward',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Агрессивный'), (1, 'Консервативный'), (2, 'Сбалансированный')], verbose_name='тип по соотношению риска/прибыли'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='type_investor',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Квалифицированный инвестор'), (1, 'Неквалифицированный инвестор')], verbose_name='тип инвестора'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='types_assets',
            field=models.TextField(blank=True),
        ),
    ]
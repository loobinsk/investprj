# Generated by Django 3.0 on 2021-08-12 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210620_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_of_birth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='drawdown_behavior',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Усреднение'), (1, 'Терпимое отношение'), (2, 'Продажа части акций'), (3, 'Закрытие портфеля')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='employment_status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Работает по найму'), (1, 'Самозанятый'), (2, 'Предприниматель'), (3, 'Не работает')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='retirement_date',
            field=models.DateField(blank=True),
        ),
    ]

# Generated by Django 3.0 on 2021-07-31 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_auto_20210730_0522'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sector',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='name',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='sector',
        ),
        migrations.AddField(
            model_name='ticker',
            name='sector',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='ticker',
            name='type_according_risk_reward',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Агрессивный'), (1, 'Консервативный'), (2, 'Сбалансированный')], default=1, verbose_name='тип по соотношению риска/прибыли'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticker',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

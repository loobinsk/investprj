# Generated by Django 3.0 on 2021-07-25 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_auto_20210722_0734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TickerValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('closing_cost', models.FloatField()),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Ticker')),
            ],
        ),
        migrations.AlterField(
            model_name='stock',
            name='ticker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Ticker'),
        ),
    ]
# Generated by Django 3.0 on 2021-06-18 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210618_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='investmen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='users.InvestmentAdvisor'),
            preserve_default=False,
        ),
    ]

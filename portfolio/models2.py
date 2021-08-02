from django.db import models
from datetime import datetime, timedelta
from .models import Ticker


class TickerValue(models.Model):
	ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE, related_name='ticker_value')
	date = models.DateField()
	closing_cost = models.FloatField()

	def get_total_value(self, client):
		today = datetime.now()
		today = datetime.strftime(today, '%Y-%m-%d')
		yesterday = datetime.now() - timedelta(1)
		yesterday = datetime.strftime(yesterday, '%Y-%m-%d')
		last_objects = self.filter(ticker__ticker__portfolio__client=client, date__range=[yesterday, today])
		value = 0
		for i in last_objects.closing_cost:
			value += i
		return value


	def __str__(self):
		return self.ticker.name

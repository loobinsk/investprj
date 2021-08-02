from django.db import models
from django.contrib.auth.models import User
from users.models import Client
from datetime import datetime, timedelta

qualified_investor = 0
unqualified_investor = 1
TYPE_INVESTOR = (
    (qualified_investor, 'Квалифицированный инвестор'),
    (unqualified_investor, 'Неквалифицированный инвестор'),
)

dollars = 0
rubles = 1
CURRENCY = (
    (dollars, 'Доллары'),
    (rubles, 'Рубли'),
)

aggressive = 0
conservative = 1
balanced = 2
TYPE_RISK = (
    (aggressive, 'Агрессивный'),
    (conservative, 'Консервативный'),
    (balanced, 'Сбалансированный'),
)

minimum_loss = 0
maximum_profit = 1
FOCUS = (
    (minimum_loss, 'Минимальные просадки'),
    (maximum_profit, 'Максимальная прибыль'),
)

# shares_of_Russian_companies = 0
# international_promotions = 1
# commodity_markets = 2
# TYPE_ASSETS = (
#     (shares_of_Russian_companies, 'Акции российских компаний'),
#     (international_promotions, 'Международные акции'),
#     (commodity_markets, 'Торговые рынки'),
# )

yes = 0
no = 1
exclusively_in_etf = 2
ETF = (
	(yes, 'Да'),
	(no, 'Нет'),
	(exclusively_in_etf, 'Только в ETF'),
	)

default = 0
Focus_on_growth = 1
Focus_on_diversification = 2
INVESTMENT_STRATEGY = (
	(default, 'по умолчанию'),
	(Focus_on_growth, 'Фокус на рост'),
	(Focus_on_diversification, 'Фокус на диверсификацию'),
	)




class Portfolio(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='portfolio')
	name = models.CharField('название', max_length=255)
	initial_investment_amount = models.PositiveIntegerField('начальная сумма инвестиций',)
	investment_horizon = models.PositiveIntegerField('инвестиционный горизонт',)
	type_investor = models.PositiveSmallIntegerField('тип инвестора', choices=TYPE_INVESTOR)
	currency = models.PositiveSmallIntegerField('валюта', choices=CURRENCY)
	maximum_allowable_drawdown = models.FloatField('максимально допустимая просадка',)
	type_according_risk_reward = models.PositiveSmallIntegerField('тип по соотношению риска/прибыли', choices=TYPE_RISK)
	focus = models.PositiveSmallIntegerField('фокус', choices=FOCUS)
	sector_blacklist = models.TextField(blank=True) 
	types_assets = models.TextField()
	ETF = models.PositiveSmallIntegerField(choices=ETF)
	investment_strategy = models.PositiveSmallIntegerField('инвестиционная стратегия', choices=INVESTMENT_STRATEGY)
	create_date = models.DateField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField()

	def __str__(self):
		return self.name

	def get_type_investor(self):
		return TYPE_INVESTOR[self.type_investor][1]

	def get_focus(self):
		return FOCUS[self.focus][1]

	def get_investment_strategy(self):
		return INVESTMENT_STRATEGY[self.investment_strategy][1]

class Ticker(models.Model):
	name = models.CharField(max_length=255)
	sector = models.CharField(max_length=255, blank=True)
	true_name = models.CharField(max_length=255, blank=True)
	type_according_risk_reward = models.CharField(max_length=255, blank=True)
	etf = models.BooleanField(blank=True, default=False)

	def __str__(self):
		return self.name

class TickerValue(models.Model):
	ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE, related_name='ticker_value')
	date = models.DateField()
	closing_cost = models.FloatField()

	def __str__(self):
		return self.ticker.name


class Stock(models.Model):
	portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='stock')
	ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE, related_name='ticker')
	share = models.FloatField()
	value_share = models.FloatField(blank=True)

	def get_total_active(self):
		today = datetime.now()
		today = datetime.strftime(today, '%Y-%m-%d')
		yesterday = datetime.now() - timedelta(1)
		yesterday = datetime.strftime(yesterday, '%Y-%m-%d')
		tk_value = self.ticker.ticker_value.filter(ticker=self.ticker, date__range=[yesterday, today]).all()
		return tk_value

	def __str__(self):
		return self.ticker.name
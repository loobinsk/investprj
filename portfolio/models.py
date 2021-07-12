from django.db import models
from django.contrib.auth.models import User
from users.models import Client


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
	maximum_allowable_drawdown = models.PositiveIntegerField('максимально допустимая просадка',)
	type_according_risk_reward = models.PositiveSmallIntegerField('тип по соотношению риска/прибыли', choices=TYPE_RISK)
	focus = models.PositiveSmallIntegerField('фокус', choices=FOCUS)
	sector_blacklist = models.TextField(blank=True) 
	types_assets = models.TextField()
	ETF = models.PositiveSmallIntegerField(choices=ETF)
	investment_strategy = models.PositiveSmallIntegerField('инвестиционная стратегия', choices=INVESTMENT_STRATEGY)
	active = models.BooleanField()

	def get_type_investor(self):
		return TYPE_INVESTOR[self.type_investor][1]

	def get_focus(self):
		return FOCUS[self.focus][1]

	def get_investment_strategy(self):
		return INVESTMENT_STRATEGY[self.investment_strategy][1]



class Stock(models.Model):
	portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='stock')
	access_to_unqualified = models.BooleanField()
	name = models.CharField(max_length=255)
	ticker = models.CharField(max_length=255)
	sector = models.CharField(max_length=255)
	quantity = models.PositiveIntegerField()
	cost_in_rubles = models.PositiveIntegerField()
	cost_in_dollars = models.PositiveIntegerField()
	share = models.PositiveIntegerField(blank=True)
from django.db import models
from django.contrib.auth.models import User
import datetime

works_for_hire = 0
self_employed = 1
entrepreneur = 2
unemployed = 3
EMPLOYMENT_STATUS = (
    (works_for_hire, 'Работает по найму'),
    (self_employed, 'Самозанятый'),
    (entrepreneur, 'Предприниматель'),
    (unemployed, 'Не работает'),
)

Averaging = 0
Tolerant_attitude = 1
Sale_of_part_of_shares = 2
Closing_portfolio = 3
DRAWDOWN_BEHAVIOR = (
    (Averaging, 'Усреднение'),
    (Tolerant_attitude, 'Терпимое отношение'),
    (Sale_of_part_of_shares, 'Продажа части акций'),
    (Closing_portfolio, 'Закрытие портфеля'),
)




class InvestmentAdvisor(models.Model):
	user = models.OneToOneField(User,
							on_delete=models.CASCADE,
							related_name='invest_advisor')
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, blank=True)
	email = models.EmailField()
	company = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.user.username


class Client(models.Model):
	investmen = models.ForeignKey(InvestmentAdvisor, on_delete=models.CASCADE, related_name='client')
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	date_of_birth = models.DateField()
	retirement_date = models.DateField()
	drawdown_behavior = models.PositiveSmallIntegerField(choices=DRAWDOWN_BEHAVIOR,)
	employment_status = models.PositiveSmallIntegerField(choices=EMPLOYMENT_STATUS,)



	def __str__(self):
		return self.name
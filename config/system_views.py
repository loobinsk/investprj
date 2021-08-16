from django.shortcuts import redirect

from yf import YFinance
from yf.portfolio import Portfolio as prtf

from users.models import Client, InvestmentAdvisor
from portfolio.models import Portfolio
from portfolio.models import Stock
from portfolio.models import Ticker
from portfolio.models import TickerValue

from django.http import HttpResponse
from .logic import Logic

from .course_control import Currency
from .ticker_list import rf_shares
from .ticker_list import shares_for_skilled_investman
from .ticker_list import american_shares
from .ticker_list import american_sectors
from .ticker_list import type_american_shares
from .ticker_list import type_rf_shares
from django.shortcuts import render
from .ticker_list import rf_sectors
from .ticker_list import BLACK_LIST



def test_prj(request):
	template = 'fwefwe.html'
	return render(request, template)

def logic_test(request):
	get_portfolio = Portfolio.objects.get(name='Портфель номер 3')
	all_portfolio = Portfolio.objects.all()

	lg = Logic()
	total_percentage = lg.get_profit_all_portfolios(all_portfolio, True)
	total_value = lg.get_profit_all_portfolios(all_portfolio, False)
	stroke = f'проценты: {total_percentage}, сумма: {total_value}'

	return HttpResponse(f'все окей бро :) {stroke}')

def add_data_for_all_shares_to_the_internal_database(request):
	yf = YFinance()
	cur = Currency()

	yf.del_all_from_db()
	yf.del_all_tickers()

	list_sectors_rf_shares = []
	for i in rf_sectors.split(','):
		list_sectors_rf_shares.append(i)

	list_sectors_american_shares = []
	for i in american_sectors.split(','):
		list_sectors_american_shares.append(i)

	list_type_rf_shares = []
	for i in type_rf_shares.split(','):
		list_type_rf_shares.append(i)

	list_type_american_shares = []
	for i in type_american_shares.split(','):
		list_type_american_shares.append(i)

	rf_shares_list = []
	for i in rf_shares.split(','):
		rf_shares_list.append(i)

	american_shares_list = []
	for i in american_shares.split(','):
		american_shares_list.append(i)


	tickers= rf_shares+american_shares
	listt = []
	for i in tickers.split(','):
		if i not in BLACK_LIST:
			listt.append(i)

	yf.add_tickers(listt)
	yf.initial_data_load(days=5)
	data = yf.get_data()
	price = cur.get_currency_price()

	for i in data:
		new_count = float(i[3])
		if i[1] in american_shares:
			new_count = float(i[3])*price

		if not Ticker.objects.filter(name=i[1]).exists():
			if i[1] in rf_shares_list:
				index = rf_shares_list.index(i[1])
				new_ticker = Ticker(name=i[1])
				new_ticker.sector = list_sectors_rf_shares[index]
				new_ticker.type_according_risk_reward = list_type_rf_shares[index]
				new_ticker.save()
			elif i[1] in american_shares_list:
				index = american_shares_list.index(i[1])
				new_ticker = Ticker(name=i[1])
				new_ticker.sector = list_sectors_american_shares[index]
				new_ticker.type_according_risk_reward = list_type_american_shares[index]
				new_ticker.save()

		get_ticker = Ticker.objects.get(name=i[1])

		if not TickerValue.objects.filter(ticker=get_ticker, date=i[2]).exists():
			new_ticker_values = TickerValue(ticker=get_ticker,
											date=i[2],
											closing_cost=new_count,
											)
			new_ticker_values.save()
	yf.__del__()
	return HttpResponse('все ок')

def get_algorithm(request):
	yf = YFinance()
	yf.del_all_from_db()
	yf.del_all_tickers()
	tickers = 'IMOEX.ME, ^GSPC,)'
	listt = []
	for i in tickers.split(','):
		listt.append(i)

	yf.add_tickers(listt)
	yf.initial_data_load()
	yf.__del__()
	return HttpResponse('все гуд')
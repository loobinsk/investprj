import re
import random
from datetime import datetime, timedelta

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from users.models import Client, InvestmentAdvisor
from portfolio.models import Portfolio
from portfolio.models import Stock
from portfolio.models import Ticker
from portfolio.models import TickerValue

from yf import YFinance
from yf.portfolio import Portfolio as prtf
from .logic import Logic
from .ticker_list import rf_shares
from .ticker_list import shares_for_skilled_investman
from .ticker_list import american_shares
from .ticker_list import american_sectors
from .ticker_list import BLACK_LIST




@login_required
def index(request):
	investmen = InvestmentAdvisor.objects.get(user=request.user)
	all_clients = Client.objects.filter(investmen=investmen).all()
	all_portfolio = Portfolio.objects.filter(client__investmen=investmen, active=True).all()

	logic = Logic()
	total_shares_value = round(logic.get_all_actual_price_portfolio(all_portfolio), 2)
	
	client_list = []
	for i in all_clients:
		client_parameters_list = []
		client_portfolios = Portfolio.objects.filter(client=i, active=True).all()
		get_portfolio_drafts = Portfolio.objects.filter(client=i, active=False).all()
		get_portfolio_drafts_count = get_portfolio_drafts.count()
		client_profit = logic.get_profit_all_portfolios(client_portfolios, True)
		client_profit = round(client_profit, 2)
		if client_profit == 0:
			client_profit = 0.0
		client_active = round(logic.get_all_actual_price_portfolio(client_portfolios), 2)

		client_parameters_list.append(i)
		client_parameters_list.append(client_profit)
		client_parameters_list.append(client_active)
		client_parameters_list.append(get_portfolio_drafts_count)
		client_list.append(client_parameters_list)

	number_of_clients = all_clients.count()
	number_of_active_portfolio = 0

	for i in all_clients:
		count = int(i.portfolio.all().count())
		number_of_active_portfolio += count

	template = 'index.html'
	context = {
		'total_value': total_shares_value,
		'all_clients': client_list,
		'number_of_clients': number_of_clients,
		'number_of_active_portfolio': number_of_active_portfolio,
		'client': Client,
	}
	return render(request, template, context)

def portfolio_view(request, pk):
	portfolio = Portfolio.objects.get(pk=pk)
	stocks = Stock.objects.filter(portfolio=portfolio)
	lg = Logic()
	target_portfolio_value = lg.get_portfolio_value(portfolio)

	sectors = []
	for i in stocks:
		sector = i.ticker.sector
		sectors.append(sector)

	sectors_dict = lg.get_prc(sectors)
	sectors_list = []
	color_count = 0
	for key, value in sectors_dict.items():
		new_list = []
		width = value*4.28
		color_count += 30
		color = f'37, {color_count}, 219'
		new_list.append(key)
		new_list.append(round(value, 2))
		new_list.append(width)
		new_list.append(color)
		sectors_list.append(new_list)

	print(sectors_list)
	template = 'view.html'
	context = {
		'sectors_list': sectors_list,
		'target_portfolio_value': target_portfolio_value,
		'stocks': stocks,
		'portfolio': portfolio,
	}
	return render(request, template, context)

def create_portfolio(request):
	yf = YFinance()
	pf = prtf()
	investmen = InvestmentAdvisor.objects.get(user=request.user)
	all_clients = Client.objects.filter(investmen=investmen)
	all_stocks = Stock.objects.all()
	all_tickers = Ticker.objects.order_by('name').all()
	all_sectors = []
	for i in all_tickers:
		all_sectors.append(i.sector)

	if request.method == 'POST':
		client_pk = None

		if request.POST['client_name'] != '':
			client_name = request.POST['client_name']
			client_description = request.POST['client_description']
			client_date_birth = request.POST['client_date_birth']
			client_retirement_date = request.POST['client_retirement_date']
			client_employment_status = request.POST['client_employment_status']
			client_drawdown_behavior = request.POST['client_drawdown_behavior']
			if not Client.objects.filter(investmen=investmen, 
								name=client_name,
								description=client_description,
								date_of_birth=client_date_birth,
								retirement_date=client_retirement_date,
								drawdown_behavior=client_drawdown_behavior,
								employment_status=client_employment_status,
								).exists():
				new_client = Client(investmen=investmen, 
									name=client_name,
									description=client_description,
									date_of_birth=client_date_birth,
									retirement_date=client_retirement_date,
									drawdown_behavior=client_drawdown_behavior,
									employment_status=client_employment_status,
									)
				new_client.save()
				client_pk = new_client.pk
			else:
				client = Client.objects.get(investmen=investmen, 
									name=client_name,
									description=client_description,
									date_of_birth=client_date_birth,
									retirement_date=client_retirement_date,
									drawdown_behavior=client_drawdown_behavior,
									employment_status=client_employment_status,
									)

				client_pk = client.pk
		else:
			client_pk = request.POST["client_pk"]

		client = Client.objects.get(pk=client_pk)
		name = request.POST['name']
		type_investmen = int(request.POST['type_investmen'])

		investment_horizon = request.POST['investment_horizon']
		investment_horizon = int(re.sub("[года|лет|год| |]", "", investment_horizon))

		currency = int(request.POST['currency'])
		initial_investment_amount = int(request.POST['initial_investment_amount'])

		maximum_allowable_drawdown = request.POST['maximum_allowable_drawdown']
		maximum_allowable_drawdown = int(re.sub("%", "", maximum_allowable_drawdown)) / 10

		type_according_risk_reward = int(request.POST['type_according_risk_reward'])
		focus_potfolio = int(request.POST['focus-potfolio'])

		etf = request.POST['etf']
		if etf == 'Да':
			etf = 0
		elif etf == 'Нет':
			etf = 1
		else:
			etf = 2

		types_assets_list = []
		for i in request.POST.getlist('types-assets'):
			types_assets_list.append(i)
		list_sectors = []
		for i in request.POST.getlist('sectors'):
			list_sectors.append(i)
		invest_strategy = int(request.POST['invest_strategy'])

		portfolio = Portfolio(
			client = client,
			sector_blacklist = list_sectors,
			name=name,
			initial_investment_amount=initial_investment_amount,
			investment_horizon=investment_horizon,
			type_investor=type_investmen,
			currency=currency,
			maximum_allowable_drawdown=maximum_allowable_drawdown,
			type_according_risk_reward = type_according_risk_reward,
			focus = focus_potfolio,
			types_assets=types_assets_list,
			ETF = etf,
			investment_strategy=invest_strategy,
			active=False,
			)

		portfolio.save()

		ticker_list = []
		for i in all_tickers:
			ticker_list.append(i.name)

		skill_shares = rf_shares+shares_for_skilled_investman
		
		list_skilled_investman = skill_shares.split(',')
		list_rf_shares = rf_shares.split(',')
		list_american_shares = american_shares.split(',')


		len_all_shares = len(ticker_list)
		len_shares_for_skilled_investman = len(list_skilled_investman)

		if type_investmen == 1:
			for i in ticker_list:
				if i not in list_skilled_investman:
					del ticker_list[i]

		if type_according_risk_reward == 0:
			for i in ticker_list:
				if i.type_according_risk_reward != 0:
					del ticker_list[i]







		yf.del_all_from_db()
		yf.del_all_tickers()
		yf.add_tickers(ticker_list)
		yf.initial_data_load()
		yf.__del__()

		pf.load_data()
		pf.exclude_loss()
		total_portfolio = pf.generate_portfolios(n=1, strategy=invest_strategy, risk=maximum_allowable_drawdown)

		total_result = {}
		shares = []
		tickers = []
		for i in total_portfolio[0]:
			shares.append(i)
		for i in pf.prof_df:
			tickers.append(i)

		count_share = 0
		for i in tickers:
			if float(shares[count_share]) != 0.0:
				untotal_share = float(shares[count_share]) / 1
				total_share = untotal_share*100
				total_share = round(total_share, 2)
				get_ticker = Ticker.objects.get(name=i)
				new_stock = Stock(
								portfolio=portfolio,
								ticker=get_ticker,
								share=total_share,
								value_share=0,
								)
				new_stock.save()
				total_result[i] = float(shares[count_share])
			count_share += 1
		pf.__del__()

		return redirect(f'/portfolio-view/{portfolio.pk}/')


	template = 'create.html'
	context = {
		'all_clients': all_clients,
		'all_stocks': all_stocks,
		'all_tickers': all_tickers,
	}
	return render(request, template, context)


def portfolio_detail(request, pk):
	lg = Logic()
	portfolio = Portfolio.objects.get(pk=pk)
	profit = round(lg.get_profitability_portfolio(portfolio, True), 2)
	shares = portfolio.stock.all()
	sectors = []
	for i in shares:
		sector = i.ticker.sector
		sectors.append(sector)

	sectors_dict = lg.get_prc(sectors)
	sectors_list = []
	color_count = 0
	for key, value in sectors_dict.items():
		new_list = []
		width = value*4.28
		color_count += 30
		color = f'37, {color_count}, 219'
		new_list.append(key)
		new_list.append(value)
		new_list.append(width)
		new_list.append(color)
		sectors_list.append(new_list)

	actual_price = round(lg.actual_price_portfolio(portfolio), 2)
	all_stocks = Stock.objects.filter(portfolio=portfolio)

	shares_list = []
	for i in all_stocks:
		_list = []
		actual_share_price = round(lg.get_profitability_share(i, date=portfolio.create_date-timedelta(1), actual_price=True, percentag_or_profit=False), 2)
		quantity = round(i.value_share/actual_share_price, 2)
		_list.append(i)
		_list.append(actual_share_price)
		_list.append(quantity)
		shares_list.append(_list)



	template = 'portfolio_detail.html'
	context = {
		'sectors_list': sectors_list,
		'shares_list': shares_list,
		'portfolio': portfolio,
		'profit': profit, 
		'actual_price': actual_price,
	}	
	return render(request, template, context)

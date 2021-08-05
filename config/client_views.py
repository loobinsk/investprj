import re
import random
from datetime import datetime, timedelta

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

from users.models import Client, InvestmentAdvisor
from portfolio.models import Portfolio
from portfolio.models import Stock
from portfolio.models import Ticker
from portfolio.models import TickerValue

from yf import YFinance
from yf.portfolio import Portfolio as prtf

from .course_control import Currency
from .logic import Logic

from .ticker_list import rf_shares
from .ticker_list import shares_for_skilled_investman
from .ticker_list import american_shares
from .ticker_list import american_sectors
from .ticker_list import BLACK_LIST


def clients_list(request):
	investmen = InvestmentAdvisor.objects.get(user=request.user)
	all_clients = Client.objects.filter(investmen=investmen).all()
	lg=Logic()

	client_list = []
	for i in all_clients:
		new_list = []
		get_portfolios = Portfolio.objects.filter(client=i, active=True)
		get_client_active = round(lg.get_all_actual_price_portfolio(get_portfolios), 2)
		new_list.append(i)
		new_list.append(get_client_active)
		client_list.append(new_list)

	template = 'client/clients.html'
	context = {
		'all_clients': client_list,
	}

	return render(request, template, context)


def client_detail(request, pk):
	lg = Logic()
	client = get_object_or_404(Client, pk=pk)
	portfolios = Portfolio.objects.filter(client=client, active=True)
	portfolios_drafts = Portfolio.objects.filter(client=client, active=False)
	portfolios_drafts_list = []

	for i in portfolios_drafts:
		_list = []
		portfolio_profit = round(lg.get_profitability_portfolio(i), 2)
		all_portfolio_active = round(lg.actual_price_portfolio(i, True), 2)
		_list.append(i)
		_list.append(portfolio_profit)
		_list.append(all_portfolio_active)
		portfolios_drafts_list.append(_list)

	initial_count = lg.get_value_all_portfolios(portfolios)
	profit = lg.get_profit_all_portfolios(portfolios, True)

	portfolios_list = []
	for i in portfolios:
		_list = []
		portfolio_profit = round(lg.get_profitability_portfolio(i), 2)
		all_portfolio_active = round(lg.actual_price_portfolio(i, dollars=True),2)
		_list.append(i)
		_list.append(portfolio_profit)
		_list.append(all_portfolio_active)
		portfolios_list.append(_list)


	template = 'client/notifies.html'
	context = {
		'profit': profit,
		'portfolios_drafts': portfolios_drafts_list,
		'initial_count': initial_count,
		'client':client,
		'portfolios': portfolios_list,
	}
	return render(request, template, context)


def new_client(request):
	name = request.POST['client_name']
	description = request.POST['client_description']
	date_birth = request.POST['client_date_birth']
	retirement_date = request.POST['client_retirement_date']
	employment_status = request.POST['client_employment_status']
	drawdown_behavior = request.POST['client_drawdown_behavior']
	new_client = Client(name=name,
						description=description,
						date_of_birth=date_birth,
						retirement_date=retirement_date,
						employment_status=employment_status,
						drawdown_behavior=drawdown_behavior,
						investmen=request.user.invest_advisor,
						)
	new_client.save()
	
	return redirect('/client-overview/')


def client_change(request, pk):
	client = Client.objects.get(pk=pk)
	client.name = request.POST['client_name']
	client.description = request.POST['client_description']
	client.date_of_birth = request.POST['client_date_birth']
	client.retirement_date = request.POST['client_retirement_date']
	client.employment_status = request.POST['client_employment_status']
	client.drawdown_behavior = request.POST['client_drawdown_behavior']
	client.save()
	return redirect('client-overview', pk)


def client_delete(request, pk):
	client = Client.objects.get(pk=pk)
	client.delete()
	return redirect('clients-list')
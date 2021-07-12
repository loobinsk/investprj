import yfinance as yf
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from users.models import Client, InvestmentAdvisor
from portfolio.models import Portfolio, Stock
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_system
from django.contrib.auth.models import User
from yf.test import test_portfolio
from yf import YFinance


def get_algorithm(request):
	a = test_portfolio.PortfolioTestCase()
	return HttpResponse('все гуд')


@login_required
def index(request):
	investmen = InvestmentAdvisor.objects.get(user=request.user)
	all_clients = Client.objects.filter(investmen=investmen)



	number_of_clients = all_clients.count()
	number_of_active_portfolio = 0

	for i in all_clients:
		count = int(i.portfolio.all().count())
		number_of_active_portfolio += count

	template = 'index.html'
	context = {
		'all_clients': all_clients,
		'number_of_clients': number_of_clients,
		'number_of_active_portfolio': number_of_active_portfolio,
		'client': Client,
	}
	return render(request, template, context)

def clients_list(request):
	investmen = InvestmentAdvisor.objects.get(user=request.user)
	all_clients = Client.objects.filter(investmen=investmen)

	template = 'client/clients.html'
	context = {
		'all_clients': all_clients,
	}
	return render(request, template, context)


def client_detail(request, pk):
	client = get_object_or_404(Client, pk=pk)
	portfolios = Portfolio.objects.filter(client=client)
	template = 'notifies.html'
	context = {
		'client':client,
		'portfolios': portfolios,
	}
	return render(request, template, context)


def new_client(request):
	name = request.POST['name']
	description = request.POST['description']
	date_birth = request.POST['date_birth']
	retirement_date = request.POST['retirement_date']
	employment_status = request.POST['employment_status']
	drawdown_behavior = request.POST['drawdown_behavior']
	new_client = Client(name=name,
						description=description,
						date_of_birth=date_birth,
						retirement_date=retirement_date,
						employment_status=employment_status,
						drawdown_behavior=drawdown_behavior,
						investmen=request.user.invest_advisor,
						)
	new_client.save()
	return redirect('homepage')

def change_pass(request):
	user = request.user
	print(user.password)
	old_password = request.POST['old_password']
	new_pass = request.POST['new_password']
	new_pass2 = request.POST['new_password2']
	if user.check_password(old_password):
		if new_pass == new_pass2:
			user.set_password(new_pass)
			user.save()
			update_session_auth_hash(request, user)
			return redirect('settings')
		else:
			return HttpResponse('пароли не совпадают.')
	else:
		return HttpResponse('старый пароль не верный.')
	return redirect('settings')

def portfolio_view(request, pk):
	portfolio = Portfolio.objects.get(pk=pk)


	template = 'view.html'
	context = {
		'portfolio': portfolio,
	}
	return render(request, template, context)


def client_change(request, pk):
	return redirect('client-overview', pk)

def client_delete(request, pk):
	client = Client.objects.get(pk=pk)
	client.delete()
	return redirect('clients-list')




def create_portfolio(request):
	investmen = InvestmentAdvisor.objects.get(user=request.user)
	all_clients = Client.objects.filter(investmen=investmen)
	all_stocks = Stock.objects.all()

	if request.method == 'POST':
		client = Client.objects.get(pk=request.POST["client_name"])
		name = request.POST['name']
		type_investmen = int(request.POST['type_investmen'])

		investment_horizon = request.POST['investment_horizon']
		investment_horizon = int(re.sub("[года|лет|год| |]", "", investment_horizon))

		currency = int(request.POST['currency'])
		initial_investment_amount = int(request.POST['initial_investment_amount'])

		maximum_allowable_drawdown = request.POST['maximum_allowable_drawdown']
		maximum_allowable_drawdown = int(re.sub("%", "", maximum_allowable_drawdown))

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
		#sectors = request.POST['sectors']
		list_sectors = []
		for i in request.POST.getlist('sectors'):
			list_sectors.append(i)
		invest_strategy = int(request.POST['invest_strategy'])

		print(name)
		print(type_investmen)
		print(investment_horizon)
		print(currency)
		print(initial_investment_amount)
		print(maximum_allowable_drawdown)
		print(type_according_risk_reward)
		print(focus_potfolio)
		print(list_sectors)
		print(invest_strategy)
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


		return redirect(f'/portfolio-view/{portfolio.pk}/')



	template = 'create.html'
	context = {
		'all_clients': all_clients,
		'all_stocks': all_stocks,
	}
	return render(request, template, context)

def register(request):
	error = ''
	if request.method == 'POST':
		first_name = request.POST['first_name']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password2']
		if password == password2:
			new_user = User.objects.create_user(username=email, password=password)
			new_user.save()
			auth_login(request, new_user)
			new_invest_advisor = InvestmentAdvisor(user=new_user, 
													first_name=first_name, 
													email=email)
			new_invest_advisor.save()
			return redirect('homepage')
		else:
			error = 'Пароли не совпадают.'


	template = 'account/register.html'
	return render(request, template, {'error': error})

@login_required
def settings(request):
	if request.method =='POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		company = request.POST['company']
		investment_advisor = get_object_or_404(InvestmentAdvisor, 
												email=request.user.invest_advisor.email,
												first_name=request.user.invest_advisor.first_name,
												last_name=request.user.invest_advisor.last_name,
												company=request.user.invest_advisor.company)
		
		investment_advisor.first_name = first_name
		investment_advisor.last_name = last_name
		investment_advisor.email = email
		investment_advisor.company = company
		investment_advisor.save()

		return redirect('settings')

	template = 'account/settings.html'
	return render(request, template)

def login(request):
	error = None
	if request.user.is_authenticated:
		return redirect('homepage')
	else:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					auth_login(request, user)
					return redirect('homepage')
			else:
				error = True
		template = 'account/login.html'
		return render(request, template, {'error': error})

def logout(request):
	logout_system(request)
	return redirect('homepage')
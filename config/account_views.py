from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from users.models import Client, InvestmentAdvisor
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_system
from django.contrib.auth.models import User
from users.models import Client, InvestmentAdvisor
from portfolio.models import Portfolio
from portfolio.models import Stock
from portfolio.models import Ticker
from portfolio.models import TickerValue
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def change_pass(request):
	user = request.user
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

@csrf_protect
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
			new_client = Client(investmen=new_invest_advisor,
								name='Сергей Иванович',
								)
			new_client.save()
			name = 'Тестовый портфель'
			initial_investment_amount = 100000
			investment_horizon= 2
			type_investor = 0
			currency = 0
			maximum_allowable_drawdown = 2.1
			type_according_risk_reward = 0
			focus = 0
			ETF = 0
			investment_strategy = 1
			new_portfolio = Portfolio(
				client = new_client,
				name=name,
				initial_investment_amount=initial_investment_amount,
				investment_horizon=investment_horizon,
				type_investor=type_investor,
				currency=currency,
				maximum_allowable_drawdown=maximum_allowable_drawdown,
				type_according_risk_reward = type_according_risk_reward,
				focus = focus,
				ETF = ETF,
				investment_strategy=investment_strategy,
				active=False,
				)
			new_portfolio.save()
			types = new_portfolio.get_type_according_risk_reward()
			for i in Ticker.objects.filter(type_according_risk_reward=types)[:10]:
				new_stock = Stock(portfolio=new_portfolio, ticker=i, share=10)
				new_stock.save()


			return redirect('homepage')
		else:
			error = 'Пароли не совпадают.'


	template = 'account/register.html'
	return render(request, template, {'error': error})

@csrf_protect
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

@csrf_protect
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

@csrf_protect
def logout(request):
	logout_system(request)
	return redirect('homepage')
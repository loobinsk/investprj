from portfolio.models import Portfolio
from portfolio.models import Ticker
from portfolio.models import TickerValue
from portfolio.models import Stock
from datetime import datetime, timedelta


class Logic():

	days = 1


	def get_all_portfolio(self):
		'''получить все портфели пользователя'''
		investmen = InvestmentAdvisor.objects.get(user=request.user)
		all_portfolio = Portfolio.objects.filter(client__investmen=investmen).all()

	def get_portfolio_value(self, portfolio):
		''' получить начальную стоимость портфеля '''
		get_shares_portfolio = Stock.objects.filter(portfolio=portfolio).all()
		count = 0

		for i in get_shares_portfolio:
			try:
				share_value_for_today = TickerValue.objects.get(ticker=i.ticker, date=portfolio.create_date-timedelta(1))
			except TickerValue.DoesNotExist:
				try:
					share_value_for_today = TickerValue.objects.get(ticker=i.ticker, date=portfolio.create_date-timedelta(2))
				except TickerValue.DoesNotExist:
					share_value_for_today = TickerValue.objects.get(ticker=i.ticker, date=portfolio.create_date-timedelta(3))
			share_value_for_today = share_value_for_today.closing_cost
			amount_of_investment =  portfolio.initial_investment_amount
			total_count = float(i.share)/100*int(amount_of_investment)
			i.value_share = total_count
			i.save()
			count += i.value_share

		return int(count)

	def get_value_all_portfolios(self, portfolios):
		''' получить начальную стоимость всех портфелей  '''
		value = 0
		for i in portfolios:
			value += int(self.get_portfolio_value(i))

		return value

	def get_profitability_share(self, share, date, percentag_or_profit, actual_price=False):
		''' получить доходность одной акции
			True = проценты
			False = число
		  '''
		yesterday = datetime.now() - timedelta(1)
		yesterday = datetime.strftime(yesterday, '%Y-%m-%d')

		ticker = share.ticker
		try:
			ticker_value_at_start_date = TickerValue.objects.get(date=date, ticker=ticker)
		except TickerValue.DoesNotExist:
			try:
				date = date - timedelta(1)
				ticker_value_at_start_date = TickerValue.objects.get(date=date, ticker=ticker)
			except TickerValue.DoesNotExist: 
				date = date - timedelta(2)
				ticker_value_at_start_date = TickerValue.objects.get(date=date, ticker=ticker)

		try:
			ticker_value_at_сurrent_date = TickerValue.objects.get(ticker=ticker, date=yesterday)
		except TickerValue.DoesNotExist:
			try:
				yesterday = datetime.now() - timedelta(2)
				yesterday = datetime.strftime(yesterday, '%Y-%m-%d')
				ticker_value_at_сurrent_date = TickerValue.objects.get(ticker=ticker, date=yesterday)
			except TickerValue.DoesNotExist:
				yesterday = datetime.now() - timedelta(3)
				yesterday = datetime.strftime(yesterday, '%Y-%m-%d')
				ticker_value_at_сurrent_date = TickerValue.objects.get(ticker=ticker, date=yesterday)


		profitability_in_number = ticker_value_at_сurrent_date.closing_cost - ticker_value_at_start_date.closing_cost

		get_percentage = profitability_in_number/ticker_value_at_start_date.closing_cost*100

		if actual_price == True:
			return ticker_value_at_сurrent_date.closing_cost

		if percentag_or_profit == True:
			return get_percentage
		else:
			return float(profitability_in_number)

	def get_profitability_portfolio(self, portfolio, percentag_or_profit=True):
		''' получить доходность портфеля
			True = проценты
			False = число
		 '''
		total_return_of_all_shares = 0
		portfolio_start_value = self.get_portfolio_value(portfolio)

		for i in portfolio.stock.all():
			date = portfolio.create_date - timedelta(self.days)
			profit = self.get_profitability_share(i, date, True)
			percent_number = profit/100*i.value_share
			total_return_of_all_shares += percent_number

		portfolio_yield = total_return_of_all_shares*100/portfolio_start_value

		if percentag_or_profit == True:
			return portfolio_yield
		else:
			return total_return_of_all_shares

	def get_profit_all_portfolios(self, portfolios, percentag_or_profit):
		''' получить доходность всех портфелей
			True = проценты
			False = число
		'''
		total_percentag = None
		initial_portfolio_value = 0
		all_portfolio_profit = 0
		for i in portfolios:
			get_portfolio_value = self.get_portfolio_value(i)
			initial_portfolio_value += get_portfolio_value

			get_portfolio_profit = self.get_profitability_portfolio(i, False)
			all_portfolio_profit += get_portfolio_profit

		if initial_portfolio_value != 0:
			total_percentag = all_portfolio_profit/initial_portfolio_value*100
		else:
			return 0

		if percentag_or_profit == True:
			return round(total_percentag, 2)
		else:
			return all_portfolio_profit



	def actual_price_portfolio(self, portfolio):
		''' получить актуальную стоимость портфеля на сегодня '''
		portfolio_profit = self.get_profitability_portfolio(portfolio=portfolio, percentag_or_profit=False)
		portfolio_start_value = self.get_portfolio_value(portfolio)

		total_value = portfolio_start_value+portfolio_profit

		return total_value

	def get_all_actual_price_portfolio(self, portfolios):
		''' получить актуальную стоимость всех портфелей '''
		value = 0
		for i in portfolios:
			actual_price_portfolio = self.actual_price_portfolio(i)
			value += actual_price_portfolio
		return value


	def get_prc(self, _list):
		''' получить словарь отфильтрованных секторов 
			
			'''
		sectors_dict = {i:_list.count(i) for i in _list}
		total_value = 0
		for key, value in sectors_dict.items():
			total_value += value

		count = 0
		meaning_other = 0
		new_dict = {}
		for key, value in sectors_dict.items():
			count += 1
			if count >= 7:
				meaning_other += value
				new_dict['Прочее'] = meaning_other
			else:
				percentage = value/total_value*100
				new_dict[key] = percentage

		sorted_values = sorted(new_dict.values(), reverse=True)
		sorted_dict = {}
		for i in sorted_values:
			for k in new_dict.keys():
				if new_dict[k] == i:
					sorted_dict[k] = new_dict[k]

		sorted_dict['Прочее'] = sorted_dict.pop('Прочее')

		return sorted_dict



















			

		









from django.contrib import admin
from .models import Portfolio, Stock, Ticker, TickerValue



class TickerValueAdmin(admin.ModelAdmin):
	list_display = ['ticker', 'date', 'closing_cost',]
	list_filter = ['ticker', 'date']
	search_fields = ['ticker', 'date']

admin.site.register(TickerValue, TickerValueAdmin)

class PortfolioAdmin(admin.ModelAdmin):
	list_display = ['client', 'name', 'create_date',]
	list_filter = ['client', 'create_date']
	list_editable = []

admin.site.register(Portfolio, PortfolioAdmin)

class StockAdmin(admin.ModelAdmin):
	list_display = ['portfolio', 'ticker', 'share',]
	list_filter = ['portfolio', 'ticker']

admin.site.register(Stock, StockAdmin)

class TickerAdmin(admin.ModelAdmin):
	list_display = ['name', 'sector', 'type_according_risk_reward',]
	list_filter = ['type_according_risk_reward', 'name', 'sector']

admin.site.register(Ticker, TickerAdmin)
from django.db import models
from users.models import Client
#from portfolio.models import Portfolio


class Template(models.Model):
	datetime = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=255)
	text = models.TextField()
	status = models.CharField(max_length=255)
	client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='%(class)s')
	#portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='notification')

	class Meta:
		abstract=True

class Notification(Template):
	pass

class Signal(Template):
	pass


from django.db import models
import datetime
from django.utils import timezone

class EquipInfo(models.Model):
	equip_name = models.CharField(max_length=200)
	equip_dept = models.CharField(max_length=200)
	price_per_head = models.IntegerField(default=0)
	date_added = models.DateTimeField('date added')
	no_in_stock = models.IntegerField(default=0)

	def __str__(self):
		return self.equip_name

	def was_recently_added(self):
		now = timezone.now()
		return now-datetime.timedelta(days=1)<=self.date_added<=now

class Attr(models.Model):
	equipment = models.ForeignKey(EquipInfo,on_delete=models.CASCADE)
	desc = models.CharField(max_length=200)
	in_wishlist = models.IntegerField(default=0)

	def __str__(self):
		return self.desc

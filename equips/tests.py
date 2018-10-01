import datetime

from django.test import TestCase
from django.utils import timezone

from .models import EquipInfo

class EquipInfoModelTests(TestCase):

	def test_was_recently_added_with_old_equipment(self):
		time = timezone.now() - datetime.timedelta(days=1,seconds=1)
		old_equipment = EquipInfo(date_added=time)
		self.assertIs(old_equipment.was_recently_added(),False)

	def test_was_recently_added_with_recent_equipment(self):
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_equipment = EquipInfo(date_added=time)
		self.assertIs(recent_equipment.was_recently_added(),True)
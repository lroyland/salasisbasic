from django.db import models
from django.utils import timezone

class School(models.Model):
	school_name = models.CharField(max_length=200)
	school_logo = models.CharField(max_length=200)

	school_address = models.CharField(max_length=500)
	school_city = models.CharField(max_length=100)
	school_state = models.CharField(max_length=100)
	school_zip = models.CharField(max_length=100)

	school_phone = models.CharField(max_length=200)

	school_principal = models.CharField(max_length=200)

	school_website = models.CharField(max_length=200)

	school_short_name = models.CharField(max_length=100)

	school_number =models.CharField(max_length=200)

	school_base_grading_scale = models.CharField(max_length=200)

	school_number_of_days_rotation = models.CharField(max_length=10)

	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.school_name


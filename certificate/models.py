from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
User=get_user_model()

class Certificates(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	csp=models.CharField(max_length=40)
	level=models.CharField(max_length=20)
	certname=models.CharField(max_length=50)
	certid=models.CharField(max_length=20)
	certified_date=models.DateField(null=False)
	expiry_date=models.DateField(null=False)
	pdf_url=models.URLField(null=False,blank=False)
	validity=models.IntegerField(null=True,blank=True)
	visibility=models.BooleanField()

	def save(self, *args, **kwargs):
		td = self.expiry_date-date.today()
		self.validity = td.days
		super(Certificates, self).save(*args, **kwargs)

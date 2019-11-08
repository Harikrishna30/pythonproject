from django.db import models

# Create your models here.

class Register(models.Model):

	name=models.CharField(max_length=30)
	email=models.CharField(max_length=50)
	mobile=models.CharField(max_length=10)
	course=models.CharField(max_length=15)
	source=models.CharField(max_length=15)
	leadstatus=models.CharField(max_length=10)
	demodate=models.DateField(blank=True)
	counsler=models.CharField(max_length=20)
	remarks=models.CharField(max_length=100)


	def __str__(self):
		return self.name


class Customer(models.Model):
	email=models.ForeignKey(Register, on_delete=models.CASCADE)
	completiondate= models.DateField()
	datejoining= models.DateField()
	coursefee= models.IntegerField()
	instructor= models.CharField(max_length=20)
	aadhar= models.CharField(max_length=12)
	customerstatus = models.CharField(max_length=9, default='ongoing') #ongoing, completed, stopped

	def __str__(self):
		return self.instructor
from django.db import models

# Create your models here.
class admin_details(models.Model):

	admin_email = models.EmailField(max_length=100)
	admin_pwd = models.IntegerField()

	class Meta:
		db_table ="admin_details" 



class User_Details(models.Model):
	name = models.CharField(max_length = 100,default=None)
	age = models.IntegerField(default=None)
	phonenumber = models.IntegerField(default=None)
	address = models.CharField(max_length=200,default=None)
	gender = models.CharField(max_length=20,default=None)
	Email = models.EmailField(max_length=100,default=None)
	password = models.CharField(max_length=100,default=None)
	City = models.CharField(max_length=100,default=None)
	State = models.CharField(max_length=100,default=None)
	Country = models.CharField(max_length = 100 ,default=None)


	class Meta:
		db_table = "User_Details"



class User_Transactions(models.Model):
	User_ID = models.CharField(max_length = 100,default=None,null = True)
	Name = models.CharField(max_length = 100,default=None,null = True)
	phonenumber = models.CharField(max_length = 100,default=None,null = True)
	email_address = models.CharField(max_length = 100,default=None,null = True)
	CINO = models.CharField(max_length = 100,default=None,null = True)
	expiry_date = models.CharField(max_length = 100,default=None,null = True)
	payment_Date = models.DateField(default=None,null = True)
	payment_Time = models.TimeField(default=None,null = True)
	Amount = models.CharField(max_length = 100,default=None,null = True)
	country = models.CharField(max_length = 100,default=None,null = True)
	Status = models.CharField(max_length = 100,default=None,null = True)
	Type_of_transaction = models.CharField(max_length = 100,default=None,null = True)
	created_link_time = models.TimeField(default=None)
	created_link_date = models.DateField(default=None)
	exempt_rules = models.CharField(max_length = 100,default=None,null = True)
	ip_address = models.CharField(max_length = 100,default=None,null = True)
	mac_address = models.CharField(max_length = 100,default=None,null = True)
	Flagged_Status = models.CharField(max_length = 100,default=None,null = True)

	class Meta:
		db_table = "User_Transactions"


		

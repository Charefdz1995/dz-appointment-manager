from django.db import models


class user(models.Model):
	first_name = models.CharField(max_length=30)
	last_name  = models.CharField(max_length=30)
	email = models.EmailField(max_length=70)
	phone_number = models.CharField(max_length = 20)
	password = models.CharField(max_length=70)
	profile_photo = models.ImageField()
	profile_Bio = models.CharField(max_length = 200)

class office(models.Model):
	office_name = models.CharField(max_length = 70)
	office_profession = models.CharField(max_length = 50)
	user = models.ForeignKey(user,on_delete=models.CASCADE)
	office_logo = models.ImageField()
	description = models.CharField(max_length = 200)
	working_times = models.CharField() # Make it with choices too  

class address(models.Model):
	wialaya = models.CharField(max_length = 20)
	town = models.CharField(max_length = 20)
	street = models.CharField(max_length = 20)
	zip_code = models.CharField(max_length = 10)
	office = models.ForeignKey(office, on_delete = models.CASCADE)

class contact(models.Model): 
	office_phone_number = models.CharField(max_length = 20)
	office_email = models.EmailField(max_length = 70)
	office = models.ForeignKey(office, on_delete = models.CASCADE)
	


class appointmenet(models.Model):
	user = models.ForeignKey(user,on_delete=models.CASCADE)
	office = models.ForeignKey(office,on_delete=models.CASCADE)
	timestamp = models.DateTimeField()
	state = models.CharField(max_length = 10)


class rating(models.Model):
	user = models.ForeignKey(user,on_delete=models.CASCADE)
	office = models.ForeignKey(office,on_delete=models.CASCADE)
	rating = models.IntegerField()
	review = models.CharField(max_length = 100)

from django.db import models

# Create your models here.
class Address(models.Model):
	name = models.CharField(max_length = 30)
	phone_no = models.CharField(max_length=10)
	door_no = models.CharField(max_length = 10)
	street = models.CharField(max_length = 50)
	locality = models.CharField(max_length = 40)
	city = models.CharField(max_length = 20)
	state = models.CharField(max_length = 20)
	pincode = models.CharField(max_length = 6)

	def __str__(self):
		return (self.name + ", " + self.door_no + ", " + self.street + ", " + self.locality + ", " + 
		self.city + ", " + self.state + ", " + self.pincode + ", Phone Number - " + self.phone_no)
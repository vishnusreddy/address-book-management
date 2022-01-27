from rest_framework import serializers
from django.db.models import fields
from address_api.models import Address

# Using ModelSerializer to simplify the task of serializing data. 
class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = '__all__'
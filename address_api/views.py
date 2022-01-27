from django.shortcuts import render

# Using these modules from rest_framework.generics to simplify the CRUD operations. 
# The documentation for these is available at https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveAPIView

# Importing the Address model and its serializer. 
from address_api.serializers import AddressSerializer
from address_api.models import Address

# Create your views here.
class DetailAddressAPIView(RetrieveAPIView):
	"""GET - This endpoint provides us a detailed view of the address from the database. We will have to provide the primary key for this."""
	queryset = Address.objects.all()
	serializer_class = AddressSerializer

class ListAddressAPIView(ListAPIView):
	"""GET - This endpoint lists all of the available addresses from the database"""
	queryset = Address.objects.all()
	serializer_class = AddressSerializer

class FilterAddressAPIView(ListAPIView):
	"""GET - This endpoint lists all of the available addresses from the database"""
	serializer_class = AddressSerializer
	def get_queryset(self):
		#queryset = Address.objects.all()
		pincode = self.kwargs['pincode']
		queryset = Address.objects.filter(pincode = pincode)
		return queryset

class CreateAddressAPIView(CreateAPIView):
	"""POST - This endpoint allows for creation/addition of a new address"""
	queryset = Address.objects.all()
	serializer_class = AddressSerializer

class UpdateAddressAPIView(UpdateAPIView):
	"""PUT - This endpoint allows for updating a specific address by passing in the id of the address to update"""
	queryset = Address.objects.all()
	serializer_class = AddressSerializer

class DeleteAddressAPIView(DestroyAPIView):
	"""DELETE - This endpoint allows for deletion of a specific address from the database"""
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
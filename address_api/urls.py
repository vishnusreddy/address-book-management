from django.urls import path
from address_api import views

urlpatterns = [
    path("all-addresses/",views.ListAddressAPIView.as_view(),name="address_list"),
    path("create/", views.CreateAddressAPIView.as_view(),name="address_create"),
    path("detail/<int:pk>", views.DetailAddressAPIView.as_view(), name = "address_detail"),
    path("update/<int:pk>/",views.UpdateAddressAPIView.as_view(),name="update_address"),
    path("delete/<int:pk>/",views.DeleteAddressAPIView.as_view(),name="delete_address")
]
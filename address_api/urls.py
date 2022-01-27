from django.urls import path, re_path
from address_api import views

urlpatterns = [
    path("all-addresses/",views.ListAddressAPIView.as_view(),name="address_list"),
    path('all-addresses/<int:pincode>/', views.FilterAddressAPIView.as_view()),
    #path("all-addresses/<int:pin>/",views.FilterAddressAPIView.as_view(),name="address_list_filter"),
    path("create/", views.CreateAddressAPIView.as_view(),name="address_create"),
    path("detail/<int:pk>/", views.DetailAddressAPIView.as_view(), name = "address_detail"),
    path("update/<int:pk>/",views.UpdateAddressAPIView.as_view(),name="update_address"),
    path("delete/<int:pk>/",views.DeleteAddressAPIView.as_view(),name="delete_address")
]
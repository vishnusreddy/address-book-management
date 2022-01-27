from django.urls import path, re_path
from address_api import views

urlpatterns = [
    path("all-addresses/",views.ListAddressAPIView.as_view(),name="address_list"),
    path('all-addresses/pincode/<int:pincode>/', views.FilterAddressAPIView.as_view()),
    path("create/", views.CreateAddressAPIView.as_view(),name="address_create"),
    path("detail/<int:pk>/", views.DetailAddressAPIView.as_view(), name = "address_detail"),
    path("detail/phone/<int:phone>/", views.DetailPhoneAddressAPIView.as_view(), name = "address_detail_phone"),
    path("update/<int:pk>/",views.UpdateAddressAPIView.as_view(),name="update_address"),
    path("delete/<int:pk>/",views.DeleteAddressAPIView.as_view(),name="delete_address")
]
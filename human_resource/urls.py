from django.urls import path
from . import views


urlpatterns = [
    path('LeaveBalance/', views.LeaveBalanceAPIView.as_view(), name="LeaveBalance"),
    path('LeaveApplication/', views.LeaveApplicationAPIView.as_view(), name="LeaveApplication"),
]
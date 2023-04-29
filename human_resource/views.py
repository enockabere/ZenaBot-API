from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import LeaveBalanceSerializer,LeaveApplicationSerializer
from .models import LeaveBalance,LeaveApplication
from rest_framework import permissions

# Create your views here.
class LeaveBalanceAPIView(ListCreateAPIView):
    serializer_class = LeaveBalanceSerializer
    queryset = LeaveBalance.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
class LeaveApplicationAPIView(ListCreateAPIView):
    serializer_class = LeaveApplicationSerializer
    queryset = LeaveApplication.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
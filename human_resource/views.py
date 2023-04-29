from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,ListAPIView
from .serializers import LeaveBalanceSerializer,LeaveApplicationSerializer
from .models import LeaveApplication
from authentication.models import LeaveBalance
from rest_framework import permissions
from authentication.renderers import UserRenderer

# Create your views here.
class LeaveBalanceAPIView(ListAPIView):
    serializer_class = LeaveBalanceSerializer
    renderer_classes = (UserRenderer,)
    queryset = LeaveBalance.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
class LeaveApplicationAPIView(ListCreateAPIView):
    serializer_class = LeaveApplicationSerializer
    renderer_classes = (UserRenderer,)
    queryset = LeaveApplication.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
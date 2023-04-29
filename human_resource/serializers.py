from rest_framework import serializers
from .models import LeaveApplication
from authentication.models import LeaveBalance


class LeaveBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveBalance
        fields = ['id', 'balance']
        
class LeaveApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplication
        fields = ['id','leave_type','start_date','end_date','date_applied']
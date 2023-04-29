from django.db import models
from authentication.models import User,LeaveBalance
from django.core.exceptions import ValidationError

# Create your models here.
 
class LeaveApplication(models.Model):
    LEAVE_TYPES = (
        ("Annual","Annual"),
        ('Sick', 'Sick'),
        ('Personal', 'Personal'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    date_applied = models.DateField(auto_now_add=True)
    
    def clean(self):
        leave_balance = LeaveBalance.objects.get(user=self.user)
        if leave_balance.balance < (self.end_date - self.start_date).days:
            raise ValidationError('Not enough leave days')
        
    def save(self, *args, **kwargs):
        leave_balance = LeaveBalance.objects.get(user=self.user)
        leave_balance.balance -= (self.end_date - self.start_date).days
        leave_balance.save()
        super().save(*args, **kwargs)

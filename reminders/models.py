from django.db import models
from django.contrib.auth.models import User

class Reminder(models.Model):
    REMINDER_METHOD_CHOICES = [
        ('sms', 'SMS'),
        ('email', 'Email'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reminders')
    reminder_datetime = models.DateTimeField()
    message = models.TextField()
    method = models.CharField(max_length=10, choices=REMINDER_METHOD_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reminder at {self.reminder_datetime} via {self.method}"

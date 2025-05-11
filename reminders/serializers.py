from rest_framework import serializers
from .models import Reminder
from datetime import datetime

class ReminderSerializer(serializers.ModelSerializer):
    date = serializers.DateField(write_only=True)
    time = serializers.TimeField(write_only=True)

    class Meta:
        model = Reminder
        fields = ['id', 'date', 'time', 'message', 'method', 'reminder_datetime']
        read_only_fields = ['reminder_datetime']

    def create(self, validated_data):
        date = validated_data.pop('date')
        time = validated_data.pop('time')
        reminder_datetime = datetime.combine(date, time)
        validated_data['reminder_datetime'] = reminder_datetime
        validated_data['user'] = self.context['request'].user  # Set user from context
        return super().create(validated_data)

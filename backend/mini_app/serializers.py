from rest_framework import serializers
from .models import Profile, Task

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'telegram_id', 'coins', 'referral_code']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'icon', 'prize', 'cooldown']
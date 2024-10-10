from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=50, unique=True)
    coins = models.IntegerField(default=0)
    referral_code = models.CharField(max_length=20, unique=True)

class Task(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    prize = models.IntegerField()
    cooldown = models.IntegerField(default=60)

class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    last_completed = models.DateTimeField(null=True, blank=True)

class Referral(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrals')
    referred = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referred_by')
    created_at = models.DateTimeField(auto_now_add=True)
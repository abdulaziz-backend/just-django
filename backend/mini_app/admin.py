from django.contrib import admin
from .models import Profile, Task, UserTask, Referral

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'telegram_id', 'coins', 'referral_code')
    search_fields = ('user__username', 'telegram_id', 'referral_code')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'prize', 'cooldown')

@admin.register(UserTask)
class UserTaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'last_completed')
    list_filter = ('task', 'last_completed')
    search_fields = ('user__username',)

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('referrer', 'referred', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('referrer__username', 'referred__username')
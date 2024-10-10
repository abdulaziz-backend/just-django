from django.core.management.base import BaseCommand
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from django.conf import settings
from mini_app.models import Profile, Referral
from django.contrib.auth.models import User
import random
import string

def start(update, context):
    telegram_id = update.effective_user.id
    username = update.effective_user.username or f"user_{telegram_id}"
    
    user, created = User.objects.get_or_create(username=username)
    profile, profile_created = Profile.objects.get_or_create(user=user, telegram_id=str(telegram_id))
    
    if profile_created:
        profile.referral_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        profile.save()

    if len(context.args) > 0:
        referral_code = context.args[0]
        try:
            referrer_profile = Profile.objects.get(referral_code=referral_code)
            if referrer_profile.user != user:
                Referral.objects.get_or_create(referrer=referrer_profile.user, referred=user)
                referrer_profile.coins += 100
                referrer_profile.save()
                update.message.reply_text("You've been referred successfully! Your friend received 100 coins.")
        except Profile.DoesNotExist:
            pass

    update.message.reply_text(f"Welcome to the Just mini-app! Your referral code is: {profile.referral_code}")

def send_user_info(update, context):
    telegram_id = update.effective_user.id
    try:
        profile = Profile.objects.get(telegram_id=str(telegram_id))
        referrals_count = Referral.objects.filter(referrer=profile.user).count()
        update.message.reply_text(f"User Info:\nCoins: {profile.coins}\nReferrals: {referrals_count}")
    except Profile.DoesNotExist:
        update.message.reply_text("User not found. Please start the bot first.")

class Command(BaseCommand):
    help = 'Runs the Telegram bot'

    def handle(self, *args, **options):
        updater = Updater(settings.TELEGRAM_BOT_TOKEN, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("info", send_user_info))

        updater.start_polling()
        updater.idle()
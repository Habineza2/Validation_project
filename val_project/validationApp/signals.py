from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserActivityLog

@receiver(post_save, sender=User)
def user_activity_log(sender, instance, created, **kwargs):
    if created:
        UserActivityLog.objects.create(user=instance, activity_type='User Created')
    else:
        UserActivityLog.objects.create(user=instance, activity_type='User Updated')
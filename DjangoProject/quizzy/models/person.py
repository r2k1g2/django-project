from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Person(models.Model):
    REQUIRED_FIELDS = ('user',)
    USERNAME_FIELD = 'username'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    description = models.TextField(max_length=450,
                                   blank=True,
                                   null=True)

    def __str__(self):
        return '{}'.format(self.user)


@receiver(post_save, sender=User)
def update_profile_signal(instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)
    instance.profile.save(**kwargs)

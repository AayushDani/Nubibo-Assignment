from django.db import models
from django.contrib.auth.models import User


class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    
    plans = (
        ('Free', 'Free'),
        ('Premium', 'Premium')
    )
    
    plan = models.TextField(choices=plans, default='Free')


    def __str__(self):
        return self.user.username + "'s Information"

    class Meta:
        verbose_name_plural = "User Information"

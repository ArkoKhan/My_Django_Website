from django.db import models
from  django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=8)
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.user.username}'s profile"
    

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token_pass = models.CharField(max_length=8)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s password reset"
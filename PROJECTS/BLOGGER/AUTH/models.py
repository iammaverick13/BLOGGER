from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    GENDER = (
        ('pria','pria'),
        ('wanita','wanita'),
        ('lain-lain','lain-lain')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255, choices=GENDER)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


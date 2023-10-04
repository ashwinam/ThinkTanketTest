from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


class AgeTbl(models.Model):
    age = models.IntegerField()

    def __str__(self) -> str:
        return str(self.age)


class HobbiesTbl(models.Model):
    hobbies = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.hobbies)


class UserTbl(AbstractUser):
    email = models.EmailField(unique=True)
    mobile_no = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)

    age = models.OneToOneField(AgeTbl, on_delete=models.CASCADE, null=True)
    hobbies = models.ManyToManyField(HobbiesTbl, blank=True)
    gender = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    # object = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return str(self.username)

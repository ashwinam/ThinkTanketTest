from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class AgeTbl(models.Model):
    age = models.IntegerField()

    def __str__(self) -> str:
        return str(self.age)


class HobbiesTbl(models.Model):
    hobies = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.hobbies)


class UserTbl(AbstractUser):
    email = models.EmailField(unique=True)
    mobile_no = models.IntegerField()
    date_of_birth = models.DateField()

    age = models.OneToOneField(AgeTbl, on_delete=models.CASCADE)
    hobbies = models.ManyToManyField(HobbiesTbl, blank=True)
    gender = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return str(self.age)

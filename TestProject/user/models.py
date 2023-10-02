from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, username, password, **extra_fields)

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
        return str(self.age)

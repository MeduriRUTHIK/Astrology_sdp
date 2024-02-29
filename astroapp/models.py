from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


# Create your models here.
class registration(models.Model):
    name = models.CharField(max_length=50)
    gender_choices = (('male', 'Male'), ('female', 'Female'), ('others', 'Others'))
    gender = models.CharField(max_length=20, choices=gender_choices)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=50)

    class Meta:
        unique_together = ('name', 'email', 'mobile')

    class Meta:
        db_table = "registration_table"

    def __str__(self):
        return self.name


class feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    rating = models.CharField(max_length=30,
                              choices=[('outstanding', 'Outstanding'), ('good', 'Good'), ('ok', 'Ok'), ('bad', 'Bad')])
    body = models.TextField()

    class Meta:
        db_table = "feedback_table"

    def __str__(self):
        return self.name


class contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    class Meta:
        db_table = "contact_table"

    def __str__(self):
        return self.name


class horoscopedb(models.Model):
    month = models.CharField(max_length=100)
    day = models.IntegerField()
    horoscope = models.CharField()

    class Meta:
        db_table = "Horoscope_table"

    def _str_(self):
        return self.month


class zodiacdb(models.Model):
    birth_month = models.CharField(max_length=255)
    birth_day = models.IntegerField()
    place_of_birth = models.CharField(max_length=255)
    astro_sign = models.CharField(max_length=255)

    class Meta:
        db_table = "Zodiac_sign"

    def _str_(self):
        return f"{self.birth_month} {self.birth_day} - {self.place_of_birth}"


class contactdb(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=200)

    class Meta:
        db_table = "contact_page"

    def _str_(self):
        return self.firstname;

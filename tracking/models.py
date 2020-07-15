from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=60)
    _id = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return self.name

class Award(models.Model):
    award_type = models.CharField(max_length=30)

    def __str__(self):
        return self.award_type

class Address(models.Model):
    attentionTo= models.CharField(max_length=50)
    companyName= models.CharField(max_length=50)
    line1= models.CharField(max_length=50)
    line2= models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    state= models.CharField(max_length=20)
    country= models.CharField(max_length=20)
    phoneNumber= models.CharField(max_length=20)

    def __str__(self):
        return self.attentionTo + " " + self.country



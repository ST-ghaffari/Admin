from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=12)

    def __str__(self):
        return self.username

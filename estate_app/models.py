from django.db import models

# Create your models here.
class Contact(models.Model):

    first_name  = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    phone = models.EmailField(max_length=50)
    select_service = models.CharField(max_length=50)
    select_price = models.CharField(max_length=50)
    comments  = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name 
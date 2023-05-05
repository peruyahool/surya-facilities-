from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField(default=0000000000, max_length=10)
    message = models.CharField(max_length=200)

class TextModel(models.Model):
    cat = models.CharField(max_length=20)
    text = models.CharField(max_length=2000)
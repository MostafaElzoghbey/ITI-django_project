from django.db import models
from authmansoura.models import *

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=False)
    description = models.CharField(max_length=150, null=False)
    is_borrowed = models.BooleanField(default=False)
    borrowed_by_id = models.ForeignKey(
        Myaccount, null=True, blank=True, on_delete=models.SET_NULL,)
    returnTime = models.DateTimeField(null=True)
    photoName = models.CharField(max_length=50, default="1.jpg")

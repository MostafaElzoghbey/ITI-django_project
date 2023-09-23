from django.db import models

# Create your models here.


class Myaccount(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=8)
    account = models.EmailField()
    is_admin = models.CharField(max_length=8, default=False)

    def __str__(self):
        return self.username

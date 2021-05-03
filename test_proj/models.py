from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
class Profile(models.Model):
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
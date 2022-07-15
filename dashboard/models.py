from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class CrudOpr(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    photo = models.ImageField(default="wallpaperflare.com_wallpaper.jpg", null=True, blank=True)
    
    
    def __str__(self): 
        return self.name
    class Meta:
        managed = False
        db_table = 'crud_opr'

class Signup(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    

    class Meta:
        managed = False
        db_table = 'auth_user'
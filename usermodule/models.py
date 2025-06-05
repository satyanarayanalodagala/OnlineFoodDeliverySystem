from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class User_signup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Gender = models.CharField(max_length=10)
    Phone= models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    def __str__(self):
        return self.user
class resturent_signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    RestName = models.CharField(max_length=10)
    Phone= models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    status=models.CharField(max_length=10,default=False)
    image1 = models.ImageField(upload_to="")
    def __str__(self):
        return self.RestName
class employe_signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Gender = models.CharField(max_length=10)
    Phone= models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    status = models.CharField(max_length=10,default=False)
    def __str__(self):
        return self.user

class Add_Food(models.Model):
    user=models.ForeignKey(resturent_signup,on_delete=models.CASCADE)
    Category= models.CharField(max_length=10)
    Name=models.CharField(max_length=25)
    region=models.CharField(max_length=25)
    vnv=models.CharField(max_length=10)
    cost= models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    def __str__(self):
        return self.user
class Order(models.Model):
    user = models.ForeignKey(User_signup, on_delete=models.CASCADE)
    food=models.ForeignKey(Add_Food, on_delete=models.CASCADE)
    quantity=models.CharField(max_length=25)
    res=models.ForeignKey(resturent_signup, on_delete=models.CASCADE)
    ordered=models.CharField(default=False)

    def __str__(self):
        return self.user
class UserOrder(models.Model):
    user = models.ForeignKey(User_signup, on_delete=models.CASCADE)
    food = models.ForeignKey(Add_Food, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=25)
    res = models.ForeignKey(resturent_signup, on_delete=models.CASCADE)
    ordered = models.CharField(default=False)

    def __str__(self):
        return self.user

class feedback(models.Model):
    usname=models.CharField(max_length=25)
    mail=models.EmailField()
    cont=models.CharField(max_length=25)
    mess=models.TextField(max_length=225)
    star=models.CharField(max_length=25)

    def __str__(self):
        return self.user




from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)
    type = models.CharField(max_length=300, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)
    description = models.TextField(blank=True)
    price = models.FloatField(default=0.0, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.



class Book(models.Model):
    
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)


    def __str__(self):
        return self.title




# class Item(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(default="description")
#     price = models.DecimalField(max_digits=10, decimal_places=2, default="price")
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return self.name





class Item(models.Model):
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
 
    def __str__(self):
        return self.name
from django.db import models
from django.db.models import Model

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    topping_name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topping_name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Picture(Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='upload/')
    date_added = models.DateTimeField(auto_now_add=True)




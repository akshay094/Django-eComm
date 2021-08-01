from django.db import models

# Create your models here.
class Products(models.Model):
  Name = models.CharField(max_length=20)
  Currency=models.CharField(max_length=3)
  Price = models.IntegerField()
  Category = models.CharField(max_length=20)
  Colors = models.CharField(max_length=100)
  Available = models.BooleanField();

  def __str__(self):
      return "{} {}{}".format(self.Name , self.Currency ,self.Price)
  
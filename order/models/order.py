from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    products = models.ManyToManyField(Product, blank=False)
    user = models.ForeignKey(User, null=False)

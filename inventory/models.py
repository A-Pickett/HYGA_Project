from django.db import models


# Create your models here.

class InventorySelector(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=100)


class MyInventory(models.Model):
    item = models.CharField(max_length=100)
    desc = models.TextField()
    loc = models.TextField()
    curr_loaned = models.BooleanField(default=False)
    image = models.CharField(max_length=100)


class BorrowedItems(models.Model):
    item = models.CharField(max_length=100)
    borrowed_from = models.CharField(max_length=100)
    desc = models.TextField()
    loc = models.TextField()
    image = models.CharField(max_length=100)


class LoanedItems(models.Model):
    item = models.CharField(max_length=100)
    lent_to = models.CharField(max_length=100)
    desc = models.TextField()
    loc = models.TextField()
    image = models.CharField(max_length=100)


from django.db import models
from django.urls import reverse


class InventoryItem(models.Model):
    item = models.CharField(max_length=100)
    desc = models.TextField()
    loc = models.TextField()
    curr_loaned = models.BooleanField(default=False)
    image = models.CharField(max_length=100)

# Creating a function to direct the user to the item detail page once they have created a new InventoryItem object
    def get_absolute_url(self):
        return reverse('inventory:item_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.item


class InventorySelector(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
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


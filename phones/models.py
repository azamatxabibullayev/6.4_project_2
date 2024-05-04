from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.name


class Phones(models.Model):
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.IntegerField()
    color = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)

    class Meta:
        db_table = 'Phone'

    def __str__(self):
        return self.model

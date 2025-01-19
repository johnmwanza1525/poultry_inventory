from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=80)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        """
        Ensure correct plural of Category
        in admin UI
        """
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Parent class for all bird products
    of different types
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.CASCADE)
    breed = models.CharField(max_length=80)
    description = models.TextField()
    plumage = models.TextField()
    is_broiler = models.BooleanField(default=False, null=True, blank=True)
    eggs_per_year = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.breed

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')  # Changed to ImageField

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    image = models.ImageField(upload_to='products/')  # Changed to ImageField
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Auto-calculate discount percentage
        if self.old_price and self.price:
            self.discount = int(((self.old_price - self.price) / self.old_price) * 100)
        super().save(*args, **kwargs)
from django.db import models
from django.contrib.auth.models import User

# Category choices
CATEGORY_CHOICES = (
    ('Water Bottle', 'Water Bottle'),
    ('Bamboo Bottle', 'Bamboo Bottle'),
    ('New Arrivals','New Arrivals'),
)

# Product model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Water Bottle')

    def __str__(self):
        return self.name

# Sale model
class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"Sale by {self.user.username if self.user else 'Unknown'} on {self.date}"



# models.py
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"

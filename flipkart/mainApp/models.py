from django.db import models
from django.conf import settings
from django.shortcuts import reverse

class Item(models.Model):
    title = models.CharField(max_length = 100)
    price = models.FloatField()
    link = models.URLField()
    slug = models.SlugField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("mainApp:cart", kwargs={"slug": self.slug})
    
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank = True,null = True)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    
    def get_absolute_user(self):
        return reverse("mainApp:buy", kwargs={"user": self.user})

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items = models.ManyToManyField(Cart)
    # ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
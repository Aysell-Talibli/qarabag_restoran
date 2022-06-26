
from django.db import models
from django.utils import timezone
class Category(models.Model):
    Categories=(('Səhər','səhər'),('Nahar','nahar'), ('Şam','şam'), 
    ('Desertlər','desertlər'))
    category = models.CharField(max_length=10, choices=Categories)
    def __str__(self):
        return self.category
    
class Menu(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image=models.ImageField(default='img/menu1.png',blank=True, null=True)
    date_posted=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
    
class Menu_category(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    category=models.ForeignKey(Menu, on_delete=models.SET_NULL,
     related_name='menu_food',
    null=True)
    price=models.IntegerField()
    def __str__(self):
        return self.name

class Gallery(models.Model):
    image=models.ImageField(blank=False,null=False)
    

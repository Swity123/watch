from django.db import models

# Create your models here.
class category(models.Model):
    watch_type = models.CharField(max_length=30)
    special = models.CharField(max_length=70)

    def __str__(self):
        return self.watch_type

class watches(models.Model):
    watch_type = models.ForeignKey(category,on_delete = models.CASCADE,default='')
    brand_name = models.CharField(max_length=20)
    price = models.FloatField()
    img = models.ImageField(upload_to='photo')
    des = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name



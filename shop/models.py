from django.db import models

# Create your models here.
class Products(models.Model):
    product_id= models.AutoField
    product_name=models.CharField(max_length=30,default='')
    product_desc=models.CharField(max_length=50,default='')
    category = models.CharField(max_length=50,default='')
    subcategory = models.CharField(max_length=50,default='')
    price=models.IntegerField(default=0)
    # publish_date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default='')
    
    def __str__(self):
        return self.product_name

class ContactUs(models.Model):
    product_id= models.AutoField(primary_key=True)
    Name = models.CharField(max_length=70,default='')
    Email = models.CharField(max_length=80,default='')
    Phone = models.CharField(max_length=10,default='')
    Text = models.CharField(max_length=500,default='')

    def __str__(self):
        return self.Name

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    time_stamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:8] + "..."

class abc(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=4000,default='')
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=70,default='')
    email = models.CharField(max_length=80,default='')
    address = models.CharField(max_length=200,default='')
    city = models.CharField(max_length=80,default='')
    state = models.CharField(max_length=80,default='')
    zip_code = models.CharField(max_length=50,default='')
    Phone = models.CharField(max_length=10,default='')

    def __str__(self):
        return self.name











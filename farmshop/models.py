from django.db import models
class Category(models.Model):
    category_name=models.CharField(max_length=64)
    number_of_searches=models.IntegerField(default=0)
    total_number_of_product=models.IntegerField(default=0)
    def __str__(self):
        return(f"{self.category_name}")
class Products(models.Model):
    name=models.CharField(max_length=32)
    company_name=models.CharField(max_length=128)
    product_price=models.IntegerField()
    image=models.ImageField(upload_to='products')
    product_desc=models.CharField(max_length=128)
    product_quantity=models.IntegerField(default=0)
    quantity_per_product=models.IntegerField(default=1)
    category_id=models.ForeignKey(Category,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return(f"{self.name}{self.product_price}")
#class Post(models.Model):
#    username=models.CharField(max_length=200)
    # password=models.CharField(max_length=64)
    # timestamp=models.DateTimeField(auto_now_add=True)
    # image=models.ImageField(upload_to="all_covers/", default="all_covers/farm.jpg")
    # def __str__(self):
    #     return f"{self.id}.{self.title}"

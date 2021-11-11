from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Product(models.Model):
    product_brand = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_feature = models.TextField()
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    image = models.FileField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    creater = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='product_pics', default='default.jpg')

    def __str__(self):
        return f'{self.product.product_name} Product image'

    def save(self):
        super().save()

        img = Image.open(self.images.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.images.path)

# Post=Product
# PostImage= ProductImage


# class PostImageAdmin(admin.StackedInline): model = PostImage

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):inlines = [PostImageAdmin] 
# class Meta:model = Post

# @admin.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):pass

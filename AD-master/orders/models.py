from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# import string
# import random
# Create your models here.
class CustomerOrder(models.Model):
    # S = 10  # number of characters in the string. 
    # order_name_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))   

    order_name_id = models.CharField(max_length=100)
    order_address = models.TextField()
    payment_method = models.CharField(max_length=100)
    product_quantity = models.IntegerField()
    product_id = models.IntegerField()
    product_Total = models.IntegerField()
    date_ordered = models.DateTimeField(default=timezone.now)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.order_name_id

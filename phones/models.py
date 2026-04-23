from django.db import models

# Create your models here.

import uuid
from datetime import date
from django.urls import reverse

class Phone(models.Model):
    phone_id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    phone_title=models.CharField(max_length=50,unique=True)
    phone_brand=models.CharField(max_length=100)
    phone_model=models.CharField(max_length=50)
    phone_price=models.DecimalField(max_digits=12,decimal_places=2)
    created_on=models.DateField(default=date.today)

    def get_absolute_url(self):
        return reverse("phone-details",kwargs={"pk":self.phone_id})
    
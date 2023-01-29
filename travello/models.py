from django.db import models

# Create your models here.


class Destination:
    id: int
    name: str
    img: str
    desc: str
    price: int

class Person(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    phone_no=models.IntegerField()
    address= models.CharField(max_length=100)
    company= models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.first_name

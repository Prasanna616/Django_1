from django.shortcuts import render
from .models import Destination,Person
# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'First Biryani, Then Sherwani'
    dest2.img = 'destination_2.jpg'
    dest2.price = 650

    dest3 = Destination()
    dest3.name = 'Bengaluru'
    dest3.desc = 'Beautiful City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 750

    dest4 = Destination()
    dest4.name = 'Gokak'
    dest4.desc = 'Karadantu nadu'
    dest4.price = 1000 

    dests = [dest1, dest2, dest3,dest4]

    return render(request, "index.html", {'dests': dests})

def about(request):
    """  
    person1 = Person()
    person1.first_name = 'Prasanna'
    person1.last_name = "Nashi"
    person1.address= "Gokak"
    person1.company = "tcs"
    person1.phone_no = 7022425616

    person2 = Person()
    person2.first_name = 'Ajit'
    person2.last_name = "Hosamani"
    person2.address= "Island"
    person2.company = "Marriot"
    person2.phone_no = 7022425555

    person = [person1, person2]
    """
    person = Person.objects.values()
    return render(request,"about.html",{'person': person })

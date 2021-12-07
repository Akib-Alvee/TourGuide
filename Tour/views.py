#from django.http import HttpResponse
from django.shortcuts  import render,HttpResponse,redirect,get_object_or_404
from .models import Contact,Destination,Booking
from math import ceil
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Booking,Destination
from users.models import User


# Create your views here.

def home(request):
    return  render(request, 'Tour/home.html')

@login_required
def tourindex(request):
    allProds = []
    catprods = Destination.objects.values('category', 'id')

    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Destination.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'Tour/tourindex.html', params)
def searchMatch(query, item):
    '''return true onlyif query matches the item'''
    if query in item.desc.lower() or query in item.Destination_name.lower() or query in item.category.lower():
        return True
    else:    
        return False 

def search(request):
    query = request.GET.get('search')
    print(query )
    allProds = []
    catprods = Destination.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Destination.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds':allProds, "msg":""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg':"Please make sure  to enter relevant query"}
    return render(request, 'Tour/search.html', params)

@login_required
def destination(request, name=""):
    thank =False

    # results = Destination.objects.values('Destination_name')
    # print(results)
    destObj = get_object_or_404(Destination,Destination_name=name,)
    amount=destObj.price
    # print(destObj.price)
    # number_of_guests = ""
    if request.method=="POST":
        print("HERE", name)
        # destination = request.POST.get('destination', '')
        departure = request.POST.get('departure', '')
        number_of_guests = ''
        number_of_guests = request.POST.get('number_of_guests','')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        trip_date = request.POST.get('trip_date', '')
        amount = amount * int(number_of_guests)
        booking = Booking(user_id=request.user,destination=name,
                          departure=departure,
                          number_of_guests= number_of_guests,
                          email=email,  phone=phone, 
                          desc=desc,  trip_date= trip_date,
                          amount = amount

                          )
        booking.save()
        thank = True

    return render(request, 'Tour/destinations.html',{"Destination":name,'thank':thank})
      
@login_required
def contact(request):
    thank =False
    if request.method=="POST":
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        tour_name = request.POST.get('tour_name', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=username, 
                          email=email, phone=phone,
                          tour_name=tour_name, 
                          desc=desc)
        contact.save()
        thank = True
    return render(request, 'Tour/contact.html',{'thank': thank})
    
    

# place view
@login_required
def placeview(request, myid):

            # Fetch the product using the id
            placeview = Destination.objects.filter(id=myid)
            return render(request, 'Tour/placeview.html', {'placeview':placeview[0]})












from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
import json
# Assuming you have a Delivery model defined in your models.py file
from .models import Delivery
from django.shortcuts import get_object_or_404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Delivery



# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')


def trackorder(request):
    return render(request, 'trackorder.html')

def backtodashboard(request):
    return render(request, 'index.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
        
    return render(request, 'login.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if password == repeatPassword:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('/')
            except:
                error_message = 'Error creating account'
                return render(request, 'signup.html', {'error_message':error_message})
        else:
            error_message = 'Password do not match'
            return render(request, 'signup.html', {'error_message':error_message})
        
    return render(request, 'signup.html')

def user_logout(request):
    logout(request)
    return redirect('/')

#delivery related stuff 
#maping the delivery related stuff
def view_delivery(request):
    return render(request, 'delivery_detail.html')
def mapinte(request):
    return render(request, 'mapinte.html')
#rendering the delivery map
def createdelivery(request):
    return render(request, 'createdelivery.html')
# Create functionality
# views.py

def create_delivery(request):
    if request.method == 'POST':
        # Extract data from the form
        delivery_address = request.POST.get('delivery_address')
        delivery_time = request.POST.get('delivery_time')
        delivery_person_name = request.POST.get('delivery_person_name')
        company_name = request.POST.get('company_name')
        item_price = request.POST.get('item_price')
        status = request.POST.get('status')
        sender_address = request.POST.get('sender_address')
        is_paid = request.POST.get('is_paid')
        new_delivery = Delivery.objects.create(
            delivery_address=delivery_address,
            delivery_time=delivery_time,
            delivery_person_name=delivery_person_name,
            company_name=company_name,
            item_price=item_price,
            status=status,
            sender_address=sender_address,
            is_paid=is_paid
        )
        # Save the delivery object
        new_delivery.save()
        # Redirect to a page showing the created delivery or any other appropriate page
        return redirect('delivery_detail', delivery_id=new_delivery.id)
    return render(request, 'create_delivery.html')


# Read functionality
def view_delivery(request, delivery_id):
    # Get the delivery object based on the delivery_id recent delivery
    current_delivery = Delivery.objects.last()  # Example: Get the latest delivery
    return render(request, 'delivery_detail.html', {'current_delivery': current_delivery})



# Update functionality



def updatedelivery(request, delivery_id):
    delivery = get_object_or_404(Delivery, pk=delivery_id)
    return render(request, 'updatedelivery.html', {'delivery': delivery, 'user': request.user})



# Delete functionality
def delete_delivery(request, delivery_id):
    # Get the delivery object based on the delivery_id
    delivery = get_object_or_404(Delivery, pk=delivery_id)
    if request.method == 'POST':
        # Delete the delivery object
        delivery.delete()
        # Redirect to a page showing remaining deliveries or any other appropriate page
        return redirect('delivery_list')
    # Pass the delivery object to the template to confirm deletion
    return render(request, 'confirm_delete_delivery.html', {'delivery': delivery})

# List all deliveries functionality
def list_deliveries(request):
    # Retrieve all delivery objects
    deliveries = Delivery.objects.all()
    # Pass the list of deliveries to the template to display
    return render(request, 'delivery_list.html', {'deliveries': deliveries})

def blockchainauth(request):
    return render(request, 'blockchainauth.html')

#blockchain part 
# views.py





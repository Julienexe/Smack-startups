from django.shortcuts import render
from .models import Teammate, Category, Stall, Product

def home(request):
    teammates = Teammate.objects.all()
    return render(request, "index.html", {"teammates": teammates})

def bsbs(request):
    # Fetch all categories from the database
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    
    return render(request, "startups/shop.html", context)

def stalls(request,category_id):
    # Fetch all categories from the database
    category = Category.objects.get(id=category_id)
    # Fetch all stalls from the database
    stalls = category.stalls.all()
    context = {
        "category": category,
        "stalls": stalls,
    }
    
    return render(request, "startups/stalls.html", context)

def stall(request, stall_id):
    # Fetch stall from the database
    stall = Stall.objects.get(id=stall_id)
    # Fetch all products from the database
    products = stall.products.all()
    context = {
        "stall": stall,
        "products": products,
    }
    
    return render(request, "startups/stall.html", context)

def how_it_works(request):
    
    context = {
        
    }
    
    return render(request, "startups/how-it-works.html", context)

def create_stall(request):
    # Handle the form submission and stall creation logic here
    if request.method == "POST":
        # Process the form data and create a new stall
        pass  # Replace with your logic

    return render(request, "startups/create_stall.html")



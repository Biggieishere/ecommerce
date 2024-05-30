from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.html import escape
from Mysite.models import Product,Cart_Item
from django.contrib.auth.decorators import login_required


def homepage(request):
    product = Product.objects.all()
    context = {"prod":product}
    print(context)
    return render(request,"index.html",context)



@login_required
def view_to_cart(request):
    cart = Cart_Item.objects.filter(user=request.user)
    context = {'Carts':cart}
    return render(request,"cart.html",context)

def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        Cart_Item.objects.create(user=request.user, product=product)
        messages.success(request,"Product sucessfully added to cart")
        print(product_id)
    return redirect('/')

def signup(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        sanitized_input = escape(username)
        
        if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
        
        elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
           
        else:
            users = User.objects.create_user(username=sanitized_input,email=email,password=password)
            users.save()

            messages.success(request, "Signed in successfully")
            return redirect("/login")
        
        
            
    return render(request,"signup.html")


def loginapp(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        
        if user is not None:
            messages.success(request, "Logged in successfully.")
            login(request,user)
            return redirect("/")
            
            
        else:
            messages.error(request, "Login failed. Incorrect username or password")
    
    return render(request,"login.html")


# Create your views here.

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect("/")

from django.shortcuts import render,redirect
from .models import User,Product
from django.contrib import messages
from django.contrib.auth import login,authenticate
# Create your views here.
def home(request):
    return render(request, 'index.html')

def error404(request):
    return render(request,'error-404.html')

def error500(request):
    return render(request,'error-500.html')

def loginn(request):
    # userr = User.objects.get(username = request.user.username)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # url = '/' + userr.slug
        if username == "" or password == "":
                messages.error(request,"Please fill all the fields")
                return redirect('login')
        else:
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                #messages.success(request,"Welcome "+ str(username))
                return redirect('/')

    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        form = User(username=username,email=email,password=password)
        form.save()
        # messages.success(request,"Welcome "+ str(username))
        return redirect('/')

    return render(request,'register.html')

def logout(request):
    return render(request,'login.html')


def profile(request):
    return render(request,'profile.html')

def product(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            username = request.user
            slug = request.user.slug
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            company_name = request.POST.get('cname')
            product_name = request.POST.get('pname')
            manufactor_name = request.POST.get('mname')
            product_number = request.POST.get('pnum')
            category = request.POST.get('category')
            landline = request.POST.get('lno')
            mobile = request.POST.get('mno')
            address1 = request.POST.get('address1')
            state = request.POST.get('state')
            address2 = request.POST.get('address2')
            postcode = request.POST.get('pcode')
            city = request.POST.get('city')
            counry = request.POST.get('country')
            form = Product(username = username,slug=slug,first_name=first_name,
            last_name=last_name,comapany_name=company_name,product_name=product_name,
            product_number=product_number,manufacturer_name=manufactor_name,
            category=category,landline_no=landline,mobile_no=mobile,address1=address1,
            address2=address2,state=state,city=city,postcode=postcode,country=counry
            )
            form.save()
            
            return redirect('/enterProduct')


            
        return render(request,'enterProduct.html')
    return redirect('login')
from django.shortcuts import render,HttpResponse
from .models import *
from product.models import about_us
from product.models import contact
from product.models import Home
from product.models import Form

# Create your views here.



def car(request):
    info=companyInformation.objects.all().first()
    products =product.objects.all()
    
    data={
       'info':info,
        'products':products
    }
    
    return render(request,'car.html',data)

def Contact(request):
   
   if request.method =='POST':
       
      name  = request.POST.get('name')
      email  = request.POST.get('email')
      comment  = request.POST.get('comment')
      new_contact = contact(name=name, email=email, comment=comment)
      new_contact.save()

      return HttpResponse("<h1> THANKS FOR CONTACT US</h1>")
   return render(request, 'contact.html')

def form(request):
   if request.method == 'POST':
      full_name = request.POST.get('full_name')
      address = request.POST.get('address')
      car_brand = request.POST.get('car_brand')
      car_model = request.POST.get('car_model')
      additional_option = request.POST.get('additional_option')
      price = request.POST.get('price')
        
      new_form = Form(
            full_name=full_name,
            address=address,
            car_brand=car_brand,
            car_model=car_model,
            additional_option=additional_option,
            price=price
        )
      new_form.save()
        
      return HttpResponse("<h1>Thanks for buying</h1>")
   return render(request, 'form.html')
    

def sign(request):
    return render(request,'sign.html')

def about(request):
    about_info = about_us.objects.all().first()
    
    
    data = {
        'about_info': about_info,
        
    }
    
    return render(request, 'about.html', data)


def home(request):
    home_info = Home.objects.all().first()
    background_image = Home.objects.first().background_image 
   
    
    data={
        'home_info':home_info,
        'background_image':background_image
        
        
    }
    return render(request, 'home.html', data)

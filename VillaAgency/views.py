from django.shortcuts import render,redirect,HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def properties(request):
    return render(request, 'properties.html')

def propertyDetails(request):
    return render(request, "property-details.html")

def contact(request):
     if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message =request.POST.get('message')

        image = request.FILES.get('image')
       
        
        contact_message=contactMessage.objects.create(name=name, email=email, 
        subject=subject,message=message, image=image)
        # if image:
        #  contact_message.image=image
        # if document:
        #  contact_message.document=document
        # if music:
        #  contact_message.music=music
        #  contact_message.save()
       
        return redirect('contact')
     else:
         return render(request,'contact.html')
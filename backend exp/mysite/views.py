from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from mysite.models import Contact, TextModel

# Create your views here.
def home(request):
    CEO = TextModel.objects.filter(cat="CEO")[0]
    OBJECTIVE = TextModel.objects.filter(cat="OBJECTIVE")[0]
    VISION = TextModel.objects.filter(cat="VISION")[0]
    BENEFITS = TextModel.objects.filter(cat="BENEFITS")[0]
    return render(request, 'home.html', {'CEO': CEO, "OBJECTIVE": OBJECTIVE, "VISION": VISION, "BENEFITS": BENEFITS})

def services(request):
    text = TextModel.objects.filter(cat="Cleaning")[0]
    return render(request, 'services.html', {'text': text})

def about_us(request):
    ABOUT = TextModel.objects.filter(cat="ABOUT")[0]
    return render(request, 'about_us.html', {'ABOUT': ABOUT})

def client(request):
    CLIENT = TextModel.objects.filter(cat="CLIENT")[0]
    return render(request, 'client.html', {'CLIENT': CLIENT})

def gallery(request):
    return render(request, 'gallery.html')

@csrf_protect
def contact_us(request):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        user = Contact.objects.create(full_name=full_name, phone=phone, email=email, message=message)
        user.save()
        return redirect('/contact_us')

    return render(request, 'contact_us.html')
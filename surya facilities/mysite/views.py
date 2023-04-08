from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from mysite.models import Contact

# Create your views here.
def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def about_us(request):
    return render(request, 'about_us.html')

def client(request):
    return render(request, 'client.html')

@csrf_protect
def contact_us(request):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        user = Contact.objects.create(full_name=full_name, email=email, message=message)
        user.save()
        return redirect('/contact_us')

    return render(request, 'contact_us.html')
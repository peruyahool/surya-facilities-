
from django.urls import path
from mysite import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('services', views.services, name="Services"),
    path('about_us', views.about_us, name="About Us"),
    path('contact_us', views.contact_us, name="Contact Us"),
    path('client',views.client, name="Client"),
    path('gallery', views.gallery, name="Gallery")
]

from django.shortcuts import render,get_object_or_404
from .models import Contact


def home(request):
    return render(request,'contact/home.html')
def contact(request):
    all_contacts = Contact.objects.all()
    return render(request, 'contact/index.html', {'contacts': all_contacts})

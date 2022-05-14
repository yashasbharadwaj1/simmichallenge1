from django.shortcuts import render
from .models import Contact
# Create your views here.
def home(request):
    all_posts = Contact.objects.all()
    return render(request, 'contact/index.html', {'posts': all_posts})


from django.shortcuts import render
from .models import Destination,Testimonials,NewsPost

# Create your views here.
def index(request):
    dests = Destination.objects.all()
    tests = Testimonials.objects.all()
    newpost = NewsPost.objects.all()
    return render(request, "index.html",{'dests':dests, 'tests': tests, 'newpost': newpost})

def contact(request):
    return render(request, 'contact.html')


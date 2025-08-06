from django.conf import settings
from django.shortcuts import render

# Create your views here.
def homepage(request):
    context={
        "resturant_name":settings.RESTURANT_NAME
    }
    return render(request,"home/index.html",context)
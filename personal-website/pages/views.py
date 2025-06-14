from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page_view(request):
    return HttpResponse("Home Page")


def about_page_view(request):
    context = {
        "name": "Thomas",
        "age": 21,
    }
    return render(request, "pages/about.html", context)

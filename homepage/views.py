from django.shortcuts import render
from .models import Books


def home(request):
    data = Books.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'homepage/home.html', context)

def info(request, pk):
    book = Books.objects.filter(pk=pk)
    context = {
        'book': book,
    }
    return render(request, 'homepage/info.html', context)

def about(request):
    return render(request, 'homepage/about.html')

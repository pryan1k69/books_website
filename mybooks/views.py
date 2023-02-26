from django.shortcuts import render, redirect
from homepage.models import Books
from django.views.generic import UpdateView, DeleteView
from .forms import BooksForm



def profile(request):
    userBooks = Books.objects.filter(user=request.user)
    context = {
        'userBooks': userBooks
    }


    return render(request, 'mybooks/profile.html', context)

def profile_info(request, slug):
    book = Books.objects.filter(slug=slug)
    context = {
        'book': book,
    }
    return render(request, 'mybooks/profile_info.html', context)



def create(request):
    error = ''
    if request.method == 'POST':
        form = BooksForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            lst = form.save(commit=False)
            # Сохраняем пользователя, когда он добавляет новую книгу
            lst.user = request.user
            lst.save()
            return redirect('home')
        else:
            error = 'Форма добавления книги неверная'
    form = BooksForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'mybooks/create.html', data)



class BooksUpdateView(UpdateView):
    model = Books
    template_name = 'mybooks/create.html'

    form_class = BooksForm


class BooksDeleteView(DeleteView):
    model = Books
    success_url = '/profile/'
    template_name = 'mybooks/delete.html'

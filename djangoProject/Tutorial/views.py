from django.shortcuts import render
from django.views import generic
from Tutorial.models import Book, Author
from django.shortcuts import redirect


def home(request):
    return render(request, 'Tutorial/home.html')


class AuthorListView(generic.ListView):
    template_name = 'Tutorial/author_list.html'

    def get_queryset(self):
        return Author.objects.all()


def addauthor(request):
    if 'name' not in request.POST:
        return render(request, 'Tutorial/addAuthor.html')
    Author(name=request.POST['name'], age=int(request.POST['age'])).save()
    return redirect('/authors')


def deleteauthor(request, pk):
    Author.objects.filter(pk=pk).delete()
    return redirect('/authors')


class BookListView(generic.ListView):
    template_name = 'Tutorial/book_list.html'

    def get_queryset(self):
        return Book.objects.all()


def addbook(request):
    if 'book' not in request.POST:
        return render(request, 'Tutorial/addBook.html', {'authors': Author.objects.all()})
    Book(book=request.POST['book'],
         author_id=Author.objects.get(name=request.POST['author']),
         released_at=request.POST['date']).save()
    return redirect('Tutorial/books')


def deletebook(request, pk):
    Book.objects.filter(pk=pk).delete()
    return redirect('Tutorial/books')


def booksbyauthor(request, pk):
    return render(request, 'Tutorial/bookByAuthor.html', {
        'books': Book.objects.filter(author_id=pk),
        'author': Author.objects.filter(id=pk)
    })

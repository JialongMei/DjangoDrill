from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre
from django.shortcuts import HttpResponse, Http404
from django.core.exceptions import *
from django.views import generic
from django.shortcuts import get_object_or_404
def searchWords(request):
    if request.method == 'POST':
        search = request.POST.get('textfield',None)
        try:
            genre_count = Genre.objects.filter(name__contains=search).count()
        except Genre.DoesNotExist:
            genre_count = 0

        try:
            book_count = Book.objects.filter(title__contains=search).count()
        except Book.DoesNotExist:
            book_count = 0

        result = genre_count + book_count
        html = "<H1>Keyword Apperance times: {}</H1>".format(result)
        return HttpResponse(html)

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 5
    context_object_name = 'book_list'
    template_name = 'books/my_arbitrary_template_name_list.html'

class BookDetailView(generic.DetailView):
    model = Book
    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk=primary_key)
        except Book.DoesNotExist:
            raise Http404('Book does not exist')

        return render(request, 'catalog/book_detail.html', context={'book': book})


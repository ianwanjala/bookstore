from django.http import HttpResponse
from .models import Book
from django.template import loader
from django.shortcuts import render, get_object_or_404


def index(request):
    """View function for home page of site."""
  #  book_list = Book.objects.order_by('title')
   # num_books = Book.objects.all().count()
    # template = loader.get_template('storecatalog/index.html')
    #context = {
     #   'book_list': book_list,
      #  'num_books': num_books,
    #}
    books=Book.objects
   # return HttpResponse(render(request, 'storecatalog/index.html', context))
    return render(request, 'storecatalog/index.html', {'books':books})
#// view function to return book details for selected book
def bookdetail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'storecatalog/bookdetail.html',{'book':book})
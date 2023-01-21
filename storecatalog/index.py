from django.http import HttpResponse
from .models import Book, Genre, Publisher
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
    books=Book.objects.all        
    #publisher=Publisher.count.get()
    #publisher.entry_set.all()
   # print(publisher)
    #genre = Genre.count.get()
   # genre.entry_set.all()
    #print(genre)

   # return HttpResponse(render(request, 'storecatalog/index.html', context))
    return render(request, 'storecatalog/index.html', {'books':books})
#// view function to return book details for selected book


def bookdetail(request, book_id):
    book_detail = get_object_or_404(Book, pk=book_id)
    genre = Genre.objects.get(pk=book_id)
    #print (genre)
    publisher=Publisher.objects.get(pk=book_id)
    #publisher=get_object_or_404(Publisher,fk=publisher)
    return render(request, 'storecatalog/bookdetail.html',{'book':book_detail})

def genrelist(request):
    genres=Genre.objects.all
  
    return render(request, 'storecatalog/genrelist.html',{'genres':genres}) 
def publisherlist(request):
    publishers=Publisher.objects.all
  
    return render(request, 'storecatalog/publisherlist.html',{'publishers':publishers})
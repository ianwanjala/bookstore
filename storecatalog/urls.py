from django.urls import path
from . import index

urlpatterns = [
    path('', index.index, name='index'),        
    path('<int:book_id>/', index.bookdetail, name='bookdetail'), 
    path('genres', index.genrelist, name='genrelist'),    
    path('publishers', index.publisherlist, name='publisherlist'), 
 

]

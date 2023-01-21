from django.db import models
import datetime
from django.utils import timezone
from django.shortcuts import get_list_or_404

#First model class Publisher
class Publisher(models.Model):
    # modelfield 1 of 1
    name = models.CharField(max_length=50,
                            help_text='Enter a publisher name, e.g., Penguin publishers')
    #Model field 2 of 1
    country = models.CharField(max_length=50)
    #model field 3 of 1
    publisher_id = models.IntegerField(unique=True, default=0)
    
    GOVERNMENT='government'
    PRIVATE='private'
    NGO='NGO'

    COMPANY_TYPE_CHOICES=[
        (GOVERNMENT,'Government'),
        (PRIVATE,'For Profit'),
        (NGO,'Not For Profit')
    ]

    
    type = models.CharField(max_length=50, null = True, choices=COMPANY_TYPE_CHOICES, default= GOVERNMENT)

    def __str__(self):
        return f' {self.name}{"-"}{self.country}{"-"}{self.type}'

#Second model class Genre
class Genre(models.Model):
    #model field 1 of 2
    genre_name = models.CharField(max_length=50,
                                  help_text='Enter a book genre, e.g., Fantasy')
    #modelfield 2 of model class 2
    genre_id = models.IntegerField(unique=True, default=0)
    image=models.ImageField(upload_to='images/',null=True)
#model field 3 of 2nd model class
    genre_summary=models.CharField(max_length=255, blank=True, help_text='Brief Description of the Genre title')
    def __str__(self):
        return f'{self.genre_name}{"-"}{self.genre_summary}{"-"}{self.image}'

#Third model class Book
class Book(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.RESTRICT)
    # model field 2/3
    image = models.ImageField(upload_to='images/', null=True, blank=True)
        #model field 3/3 and other consecutive fields
    publisher = models.ForeignKey(Publisher, on_delete=models.RESTRICT,null=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=13)
    price = models.IntegerField(default=0)
    publish_year = models.DateField('date published', null=True
    )
#currency converter
    KE_SHILLINGS = 'Kshs'
    DOLLAR = 'Dollar'
    EURO = 'Euro'
    BR_POUND = 'Pound'

    CURRENCY_CHOICES = [
        (KE_SHILLINGS, 'Kenya Shillings'),
        (DOLLAR, 'US Dollars'),
        (EURO, 'Euros'),
        (BR_POUND, 'Pounds')
    ]

    sale_currency = models.CharField(
        max_length=10, choices=CURRENCY_CHOICES, default=KE_SHILLINGS)

    sku = models.CharField(max_length=5, default=0000, null=False)

    def __str__(self):
        return f'{self.title}{"-"}{self.image}{"-"} {self.author} {"-"} {self.sale_currency} {self.price}'

    def getgenre(self):
        return self.genre.genre_name

    def getpublisher(self):
        return self.publisher.name

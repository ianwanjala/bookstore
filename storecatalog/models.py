from django.db import models
import datetime
from django.utils import timezone


class Publisher(models.Model):
    name = models.CharField(max_length=50,
                            help_text='Enter a publisher name, e.g., Penguin publishers')
    country = models.CharField(max_length=50)
    publisher_id = models.IntegerField(unique=True, default=0)

    def __str__(self):
        return f'{self.publisher_id} {self.name}'


class Genre(models.Model):
    genre_name = models.CharField(max_length=50,
                                  help_text='Enter a book genre, e.g., Fantasy')
    genre_id = models.IntegerField(unique=True, default=0)

    def __str__(self):
        return f'{self.genre_name}'


class Book(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.RESTRICT)
    # adding image view
    image = models.ImageField(upload_to='images/', null=True, blank=True)
        #added null=true for first data
    publisher = models.ForeignKey(Publisher, on_delete=models.RESTRICT,null=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=13)
    price = models.IntegerField(default=0)
    publish_year = models.DateField('date published', null=True
    )

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
        return f'{self.title} {"-"}{self.image}{"-"} {self.author} {"-"} {self.sale_currency} {self.price}'

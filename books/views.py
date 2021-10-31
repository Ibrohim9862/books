from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Book, Category

# Create your views here.

class HomePageView(ListView):
    model = Category
    context_object_name = 'object'
    template_name='index.html'

class Muqova(ListView):
    queryset=Book.pulicmanager.all()
    paginate_by = 4
    context_object_name = 'object'
    template_name='booklist.html'

class AllBooks(ListView):
    model = Book
    paginate_by = 4
    context_object_name = 'object'
    template_name='booklist.html'

class BookListView(ListView):
    model=Book
    paginate_by = 4
    context_object_name = 'object'
    template_name='booklist.html'

    def get_queryset(self, **kwargs):
        book = super().get_queryset(**kwargs)
        print(book.filter(catogory__id=self.kwargs['pk']))
        print(self.kwargs['pk'])
        return book.filter(catogory__id=self.kwargs['pk'])

class BookdetailView(DetailView):
    model = Book
    context_object_name='object'
    template_name='book_detail.html'
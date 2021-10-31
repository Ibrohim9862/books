from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    image=models.ImageField(upload_to='books_catogory/')

    def image_tag(self):
        return mark_safe('<img src="%s" alt="" width="80" heigth="60">' %(self.image.url))

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_list', kwargs={'pk': self.pk})
    

class Author(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    image=models.ImageField(upload_to='author/')

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" heigth="60">' % (self.image.url))

    def __str__(self):
        return self.title

class BookManager(models.Manager):
    def get_queryset(self):
        return super(BookManager, self).get_queryset().filter(bookimagem__image__isnull=True)
    
class Book(models.Model):
    catogory=models.ForeignKey(Category, on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='book_frist/')
    slug=models.SlugField(null=True,unique=True)
    add_created_day=models.DateField(auto_now=True)
    book_add_day=models.DateField(auto_now_add=True)
    book_created_day=models.DateField(blank=True, null=True)
    discription = models.TextField(null=True, blank=True)
    pulicmanager=BookManager()
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" heigth="60">' % (self.image.url))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug=self.slug or self.slugify(self.title)
        return super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse('book_detail',kwargs={ 'kwargs':self.slug})
    

class BookImageM(models.Model):
    book_muqova=models.ForeignKey(Book,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='book_muqova/')

    
    def image_tag(self):
        return mark_safe('<img src="%s" alt="" width="80" heigth="60">' %(self.image.url))




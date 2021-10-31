from django.contrib import admin

from .models import Author, Book, BookImageM, Category

# Register your models here.

class CategoryAtribute(admin.ModelAdmin):
    list_display=('title','image_tag')

admin.site.register(Category,CategoryAtribute)


class BookAtribute(admin.ModelAdmin):
    list_display=('title','book_created_day','image_tag')

admin.site.register(Book,BookAtribute)

class BookImageMAtribute(admin.ModelAdmin):
    list_display=('book_muqova','image_tag',)
admin.site.register(BookImageM,BookImageMAtribute)

class AuthorAtribute(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(Author,AuthorAtribute)



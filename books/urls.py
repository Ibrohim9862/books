from django.urls import path
from .views import(BookListView,AllBooks, BookdetailView, HomePageView, Muqova)

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('allbooks/',AllBooks.as_view(),name='allbooks'),
    path('muqova/',Muqova.as_view(),name='muqova'),
    path('<int:pk>', BookListView.as_view(),name='book_list'),
    path("<slug:slug>", BookdetailView.as_view(), name="book_detail")
]

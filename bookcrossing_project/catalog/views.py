from django.shortcuts import render

from data import BOOKS

def index_view(request):
    context = {'books':BOOKS}
    return render(request, 'catalog/index.html', context)


def categories_view(request):
    return render(request, 'catalog/categories.html')


def category_detail_view(request, category_id):
    return render(request, 'catalog/category.html')


books_ = {book['id']:book for book in BOOKS}

def book_detail_view(request, book_id):
    context ={'book': books_[book_id]}
    return render(request, 'catalog/book.html', context)
from data import BOOKS, CATEGORIES

from django.http import Http404
from django.shortcuts import render


def index_view(request):
    # BOOKS = Получение объектов из БД
    context = {'books': BOOKS}
    return render(request, 'catalog/index.html', context)


def categories_view(request):
    return render(
        request,
        'catalog/categories.html',
        {"categoties": CATEGORIES}
    )


def category_detail_view(request, id):
    return render(request, 'catalog/category.html')


def book_detail_view(request, id):
    for book in BOOKS:
        if book['id'] == id:
            context = {'book': book}
            return render(request, 'catalog/book.html', context)
    raise Http404

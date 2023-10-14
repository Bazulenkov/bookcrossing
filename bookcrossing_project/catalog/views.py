from django.shortcuts import render


def index_view(request):
    return render(request, 'catalog/index.html')


def categories_view(request):
    return render(request, 'catalog/categories.html')


def category_detail_view(request, id):
    return render(request, 'catalog/category.html')


def book_detail_view(request, id):
    return render(request, 'catalog/book.html')

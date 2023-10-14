from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('categories/', views.categories_view, name='categories'),
    path('categories/<int:category_id>', views.category_detail_view, name='category_detail'),
    path('book/<int:book_id>', views.book_detail_view, name='book_detail'),
    path('', views.index_view, name='index'),
]

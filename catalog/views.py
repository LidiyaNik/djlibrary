from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    
    """
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()

    num_genre=Genre.objects.all().count()
    
    # Доступные книги (статус = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Метод 'all()' применен по умолчанию.
    
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors, 'num_genre':num_genre},
    )
    """
    В конце функции index вызывается функция  render(), которая,
    в качестве ответа, создает и возвращает страницу HTML  
    В качестве параметров ей передаются объект request  
    (типа HttpRequest), шаблон HTML-страницы с метками 
    (placeholders), которые будут замещены данными,  а также 
    переменной context (словарь Python, который содержит данные,
    которые и будут замещать метки в шаблоне). 
    """

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    #context_object_name = 'my_book_list'   # ваше собственное имя переменной контекста в шаблоне
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    #template_name = 'books/my_arbitrary_template_name_list.html'  # Определение имени вашего шаблона и его расположения

    #Переопределение методов в классах отображения
#def get_queryset(self):
       # return Book.objects.filter(title__icontains='war')[:5] # Получить 5 книг, содержащих 'war' в заголовке

def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(BookListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    model = Book

def book_detail_view(request,pk):
    try:
        book_id=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
    
    return render(
        request,
        'catalog/book_detail.html',
        context={'book':book_id,}
    )
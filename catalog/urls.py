from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    #Додаткові настройки
    #url(r'^/url/$', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
    #url(r'^/anotherurl/$', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),

]
from django.shortcuts import  render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Страница приложения news')


def categories(request):
    return HttpResponse('<p>Статьи по категориям</p>')


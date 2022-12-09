from django.shortcuts import  redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse('Страница приложения news')


def categories(request, catslug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<p>Category page</p><p>{catslug}</p>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('start_page')
    return HttpResponse(f'Архив по годам<h1>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</p>')


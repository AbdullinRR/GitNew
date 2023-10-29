from django.shortcuts import render
from django.http import HttpResponse


def index_page(request):
    return HttpResponse('Hello, world')


def about_us_page(request):
    return HttpResponse('Здесь будет информация о нас!')


def about_us_info(request):
    return HttpResponse('Дополнительная информация!')
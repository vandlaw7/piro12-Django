from django.http import HttpResponse
from django.shortcuts import render


def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))

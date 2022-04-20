from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
from os import scandir
from django.conf import settings


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    return HttpResponse(f'Work DIR content {settings.BASE_DIR} :<br>{make_dir_tree(settings.BASE_DIR)}')


def make_dir_tree(dir_, lvl=''):
    ignore_names = ['__pycache__']
    result = ''
    dir_content = sorted(scandir(dir_), key=lambda x: not x.is_dir())
    for dc in dir_content:
        if dc.is_dir(follow_symlinks=False) and dc.name not in ignore_names:
            files = make_dir_tree(dc.path, lvl + '--')
            result += lvl + '|_ ' + str(dc.name) + '<br>' + files
        elif dc.name not in ignore_names:
            result += lvl + '| ' + str(dc.name) + '<br>'
    return result

from django.shortcuts import render


def index(request):
    return render(request, 'index/home.html')

def htmlCss(request):
    return render(request, 'index/html&css.html')

def javaScript(request):
    return render(request, 'index/javascript.html')

def python(request):
    return render(request, 'index/python.html')


def php(request):
    return render(request, 'index/php.html')

from django.shortcuts import render
from django.http import HttpResponse

def products(request, productid=1):
 output = "<h2>Продукт № {0}</h2>".format(productid)
 return HttpResponse(output)
def users(request, id=1, name='Максим'):
    output = '<h2>Пользователь</h2><h3>id: {0} Имя: {1}</h3>'.format(id, name) 
    return HttpResponse(output)


def index(request):
 cat = ["Ноутбуки", "Принтеры", "Сканеры", "Диски", "Шнуры"]
 return render(request, "index.html", context={"cat": cat})
def about(request):
    return render(request, "about.html")
def contact(request):
    return HttpResponse("<h2>Koнтaкты</h2>")

def products(request, productid = 1):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)


    
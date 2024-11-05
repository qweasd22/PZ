from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person
from django.http import HttpResponseNotFound
from django.http import HttpResponse
# Create your views here.


# def products(request, productid=1):
#  output = "<h2>Продукт № {0}</h2>".format(productid)
#  return HttpResponse(output)
# def users(request, id=1, name='Максим'):
#     output = '<h2>Пользователь</h2><h3>id: {0} Имя: {1}</h3>'.format(id, name) 
#     return HttpResponse(output)


# def index(request):
#  cat = ["Ноутбуки", "Принтеры", "Сканеры", "Диски", "Шнуры"]
#  return render(request, "index.html", context={"cat": cat})
# def about(request):
#     return render(request, "about.html")
# def contact(request):
#     return HttpResponse("<h2>Koнтaкты</h2>")

# def products(request, productid = 1):
#     output = "<h2>Продукт № {0}</h2>".format(productid)
#     return HttpResponse(output)

def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})
# сохранение данных в БД
def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")
# изменение данных в БД
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")
# удаление данных из БД
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")
    
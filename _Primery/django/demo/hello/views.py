from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return HttpResponse('<h1>Первая страница</h1>')

def test(request,name,age):
    return HttpResponse(f"""
        <h2>Имя: {name}</h2>
        <h2>Возраст: {age}</h2>
    """)

def user(request,name,age):
    return HttpResponse(f"""
        <h2>Имя: {name}</h2>
        <h2>Возраст: {age}</h2>
    """)

def user2(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    return HttpResponse(f"""
        <h2>Имя: {name}</h2>
        <h2>Возраст: {age}</h2>
    """)

def demo_data(request):
    # data = {"name":"Иван","age":20}
    # return render(request,'index.html',context=data)
    return render(request, 'index.html')

def show_form(request):
    # data = {"name":"Иван","age":20}
    # return render(request,'index.html',context=data)
    return render(request, 'form.html')

def postform(request):
    name = request.POST.get("name","Вы ничего не передали")
    age = request.POST.get("age", 0)
    return HttpResponse(f"""
            <h2>Имя: {name}</h2>
            <h2>Возраст: {age}</h2>
        """)
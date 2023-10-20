from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'templatesProductos/home.html')

def anuel(request):
    data={
        "op": 1,
        "nombre":"Anuel",
        "edad": "30 años",
        'nombrereal':"Emmanuel Gazmey Santiago",
        'genero':"Reguetón; Trap latino",
        'imagen':'imagenes/anuel.jpg'
    }
    return render(request,'templatesProductos/home.html',data)

def almighty(request):
    data={
       "op": 1,
        "nombre":"Almighty",
        "edad": "28 años",
        'nombrereal':"Alejandro Mosqueda Paz",
        'genero':"Reguetón; Pop",
        'imagen':'imagenes/alm.png'
    }
    return render(request,'templatesProductos/home.html',data)

def luar(request):
    data={
        "op": 1,
        "nombre":"Luar",
        "edad": "23 años",
        'nombrereal':"Raúl Armando Del Valle Robles",
        'genero':"Trap latino",
        'imagen':'imagenes/luar.jpg'
    }
    return render(request,'templatesProductos/home.html',data)
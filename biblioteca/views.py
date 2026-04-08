from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/lista.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        Libro.objects.create(
            titulo=request.POST['titulo'],
            autor=request.POST['autor'],
            editorial=request.POST['editorial'],
            anio=request.POST['anio'],
            disponible=request.POST.get('disponible') == 'on'
        )
        return redirect('lista_libros')
    return render(request, 'biblioteca/crear.html')

def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)

    if request.method == 'POST':
        libro.titulo = request.POST['titulo']
        libro.autor = request.POST['autor']
        libro.editorial = request.POST['editorial']
        libro.anio = request.POST['anio']
        libro.disponible = request.POST.get('disponible') == 'on'
        libro.save()
        return redirect('lista_libros')

    return render(request, 'biblioteca/editar.html', {'libro': libro})

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.delete()
    return redirect('lista_libros')
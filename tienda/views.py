from django.shortcuts import render
from tienda.models import Producto, CategoriaProd

# Create your views here.

def tienda(request):

    productos=Producto.objects.all()

    return render(request, 'tienda/tienda.html', {'productos': productos})


def categoriaProd(request, categoriaProd_id):

    categoriaProd=CategoriaProd.objects.get(id=categoriaProd_id)

    productos=Producto.objects.filter(categoriasProd=categoriaProd)

    return render(request, 'tienda/categoriaProd.html', {'categoriaProd': categoriaProd, 'productos': productos})
  
from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto, Subcategoria, Categoria

class CatalogoView(ListView):
    model = Producto
    template_name = 'catalogo.html'
    context_object_name = 'productos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

    def get_queryset(self):
        subcategoria_id = self.request.GET.get('subcategoria', None)
        if subcategoria_id:
            return Producto.objects.filter(subcategoria_id=subcategoria_id)
        return Producto.objects.all()

def home_page(request):
    productos = Producto.objects.all()
    return render(request, 'home_page2.html', {'productos': productos})

from django.contrib import admin
from .models import Categoria, Filme

# Habilita a categoria no painel com barra de busca
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    
# Habilita os filmes com busca e filtros laterais
@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'ano', 'categoria')
    search_fields = ('titulo',)
    list_filter = ('categoria',)
    
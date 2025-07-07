from django.contrib import admin
from django.utils.html import format_html
from .models import Project
from .forms import ProjectAdminForm

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ('title', 'author', 'views', 'likes', 'created_at', 'thumbnail_preview')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'author', 'description')
    readonly_fields = ('views', 'likes', 'created_at', 'updated_at', 'thumbnail_preview')
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'slug', 'author', 'description')
        }),
        ('Mídia', {
            'fields': ('thumbnail', 'access_link')
        }),
        ('Prévia', {
            'fields': ('thumbnail_preview',),
            'classes': ('collapse', 'wide')
        }),
        ('Estatísticas', {
            'fields': ('views', 'likes')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def thumbnail_preview(self, obj):
        if obj and obj.thumbnail:
            return format_html('<img src="{}" style="max-height: 150px; max-width: 200px;" />', obj.thumbnail.url)
        return "Nenhuma miniatura disponível. Faça upload de uma imagem e salve para visualizar a prévia."
    
    # Define a descrição que aparecerá como título da seção
    thumbnail_preview.short_description = 'Prévia da Miniatura'
    
    # Garante que o campo de preview seja somente leitura
    def get_readonly_fields(self, request, obj=None):
        # Se for uma edição (já existe um objeto)
        if obj:
            return self.readonly_fields + ('slug',)
        # Se for um novo objeto, não mostra o preview ainda
        return self.readonly_fields + ('thumbnail_preview',)

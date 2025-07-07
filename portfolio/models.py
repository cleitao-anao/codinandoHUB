from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='project_thumbnails/', verbose_name='Miniatura')
    author = models.CharField(max_length=100, verbose_name='Autor')
    views = models.PositiveIntegerField(default=0, verbose_name='Visualizações')
    likes = models.PositiveIntegerField(default=0, verbose_name='Curtidas')
    access_link = models.URLField(verbose_name='Link de Acesso')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Gera o slug apenas se for um novo objeto ou se o título ou autor foram alterados
        if not self.slug or 'title' in kwargs.get('update_fields', []) or 'author' in kwargs.get('update_fields', []):
            base_slug = slugify(f"{self.title}")
            self.slug = base_slug
            
            # Garante que o slug seja único
            counter = 1
            while Project.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
                
        super().save(*args, **kwargs)

    def increment_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def increment_likes(self):
        self.likes += 1
        self.save(update_fields=['likes'])

    def get_absolute_url(self):
        return reverse('portfolio:project_detail', kwargs={'slug': self.slug})

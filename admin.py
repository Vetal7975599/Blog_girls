from django.contrib import admin
from .models import Post, Comment

# Здесь происходит настройка моделей для отображения в admin панели Django.

# Отображение полей в админке по разным областям
class PostAdmin(admin.ModelAdmin):
    # Отображение полей в основном окне списка постов, информация о них.
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # Лист по каким полям будет сорртирвока списка богов
    list_filter = ('status', 'created', 'publish', 'author')
    # Лист по каким полям будем производить поиск
    search_fields = ('title', 'body')
    # Гинерация slug из заголовка, автоматически создает при создании поста
    prepopulated_fields = {'slug': ('title',)}
    # Добавляет список пользоватеей для создании автора статьи
    raw_id_fields = ('author',)
    # Под строкой поиска, будет сразу возможность переода по датам
    date_hierarchy = 'publish'
    # Порядок отображения по умолчанию
    ordering = ['status', 'publish']

# Регистррируем модель Post из Models в админке Django
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

admin.site.register(Comment, CommentAdmin)
from django.contrib import admin
from django.utils.html import mark_safe
from .models import Game, Comment, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'players', 'image_tag')
    readonly_fields = ('image_tag',)

    fields = (
        'title',
        'description',
        'players',
        'rules',
        'image',
        'image_tag',
        'tags',
    )

    filter_horizontal = ('tags',)
    search_fields = ('title', 'description')
    list_filter = ('tags',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="150" height="150" style="object-fit: cover;" />'
            )
        return 'Нет изображения'

    image_tag.short_description = 'Превью'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'game', 'created_at')
    search_fields = ('author', 'text')
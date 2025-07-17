from django.contrib import admin, messages
from .models import Women, Category


class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщин'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Незамужем')
        ]
    
    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        return queryset.filter(husband__isnull=True)
    

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'content', 'cat', 'husband', 'tags', )
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brief_info', )
    list_display_links = ('title', )
    ordering = ('time_create', 'title', )
    list_editable = ('is_published', )
    list_per_page = 5
    actions = ('set_published', 'set_draft', )
    search_fields = ('title__startswith', 'cat__name', )
    list_filter = (MarriedFilter, 'cat__name', 'is_published', )
    filter_horizontal = ('tags', )
    filter_vertical = ('tags', )

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, women: Women):
        return f'Описание {len(women.content)} символов.'
    
    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записей', messages.SUCCESS)

    @admin.action(description='Снять с публикации')
    def set_draft(self, request, qeuryset):
        count = qeuryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f'Снято с публикации {count} записей', messages.WARNING)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name', )
from django.contrib import admin
from .models import Category, Type
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Gợi ý trường slug theo category name
    list_display = ('name', 'slug')


class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Gợi ý trường slug theo type name
    list_display = ('name', 'slug')


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)

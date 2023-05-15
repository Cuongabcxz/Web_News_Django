from django.contrib import admin

from utility.models import Utility


# Register your models here.
class UtilityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Gợi ý trường slug theo title
    list_display = ('name', 'slug')


admin.site.register(Utility, UtilityAdmin)

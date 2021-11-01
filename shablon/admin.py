from django.contrib import admin
from shablon.models import Gullar, Kategoriya

# Register your models here.

class GullarAdmin(admin.ModelAdmin):
    list_display = ('nomi','narxi')
    list_display_links = ('nomi',)
    search_fields = ('nomi',)


class KategoriyaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nomi',)
    list_display_links = ('nomi',)
    search_fields = ('nomi',)


admin.site.register(Kategoriya, KategoriyaAdmin)
admin.site.register(Gullar, GullarAdmin)

# Register your models here.

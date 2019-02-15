from django.contrib import admin
from .models import Class, Career,Info

# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_name','code','subject','grade')
    search_fields = ('class_name','code')

admin.site.register(Class,ClassAdmin)
admin.site.register(Career)
admin.site.register(Info)


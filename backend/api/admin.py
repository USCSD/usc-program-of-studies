from django.contrib import admin
from .models import Class, Career

# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    site_header = "USC Administration"
    site_title = "Program of Studies Admin"
    index_title = "Program of Studies Administration"
    list_display = ('class_name','code','subject','grade')

admin.site.register(Class,ClassAdmin)
admin.site.register(Career)

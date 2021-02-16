from django.contrib import admin
from .models import Class, Career, Info
from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.


class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'code', 'subject', 'grade', 'viewable')
    search_fields = ('class_name', 'code')
    filter_horizontal = ('careers',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '70'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 8, 'cols': 100})},
    }


class CareerAdmin(admin.ModelAdmin):
    search_fields = ('career_name', 'description')
    filter_horizontal = ('suggested_classes',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '70'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 8, 'cols': 150})},
    }


admin.site.register(Class, ClassAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(Info)

from django.contrib import admin
from .models import predmet, uchet

# Register your models here.

class predmetAdmin(admin.ModelAdmin):
    fieldsets1 = [
        ('id', {'fields': ['id']}),
        ('nazvanie', {'fields': ['nazvanie']}),
        ('time', {'fields': ['time']}),
        ('audit', {'fields': ['audit']}),
    ]

class uchetAdmin(admin.ModelAdmin):
    fieldsets2 = [
        ('id', {'fields': ['id']}),
        ('login', {'fields': ['login']}),
        ('passw', {'fields': ['passw']}),
        ('propusk', {'fields': ['propusk']}),
    ]

admin.site.register(predmet, predmetAdmin)
admin.site.register(uchet, uchetAdmin)
from django.contrib import admin
from .models import car, order

# Register your models here.

class carAdmin(admin.ModelAdmin):
    fieldsets1 = [
        ('id', {'fields': ['id']}),
        ('moddel', {'fields': ['moddel']}),
        ('voditel', {'fields': ['voditel']}),
        ('nomer', {'fields': ['nomer']}),
        ('online', {'fields': ['online']}),
    ]

class orderAdmin(admin.ModelAdmin):
    fieldsets2 = [
        ('id', {'fields': ['id']}),
        ('nomer', {'fields': ['nomer']}),
        ('voditel', {'fields': ['voditel']}),
        ('passajir', {'fields': ['passajir']}),
        ('naznach', {'fields': ['naznach']}),
        ('sms', {'fields': ['sms']}),
    ]

admin.site.register(car, carAdmin)
admin.site.register(order, orderAdmin)
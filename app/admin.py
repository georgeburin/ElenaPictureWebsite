from django.contrib import admin
from .models import Picture

# Register your models here.
# class PictureAdmin(admin.ModelAdmin):
#   readonly_fields = ('id',)

admin.site.register(Picture)

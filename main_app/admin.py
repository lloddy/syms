from django.contrib import admin

# Register your models here.
from .models import Sym, Feeding, Affliction, Photo

admin.site.register(Sym)
admin.site.register(Feeding)
admin.site.register(Affliction)
admin.site.register(Photo)


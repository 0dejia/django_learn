from django.contrib import admin
from blog.models import category, navigate

# Register your models here.

class CateAdmin(admin.ModelAdmin):
	pass

admin.site.register(category, CateAdmin)
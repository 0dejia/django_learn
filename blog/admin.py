from django.contrib import admin
from blog.models import category, navigate, article

# Register your models here.

class CateAdmin(admin.ModelAdmin):
	pass

admin.site.register([category, navigate, article], CateAdmin)
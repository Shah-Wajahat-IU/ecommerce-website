from django.contrib import admin

from categories.models import Categories

class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display =('category_name','slug')

# Register your models here.
admin.site.register(Categories,categoryAdmin)

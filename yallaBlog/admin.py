from django.contrib import admin

# Register your models here.

from .models import posts,category_table
# register the models
admin.site.register(posts)
admin.site.register(category_table)

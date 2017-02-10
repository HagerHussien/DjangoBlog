from django.contrib import admin

# Register your models here.

from .models import posts,category_table,badword,Comment
# register the models
admin.site.register(posts)
admin.site.register(category_table)
# admin.site.register(subscribe)
admin.site.register(badword)
#admin.site.register(Reply)
admin.site.register(Comment)



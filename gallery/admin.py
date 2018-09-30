from django.contrib import admin
from .models import Editor,Category,Location,Image

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)


admin.site.register(Editor)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image,ImageAdmin)
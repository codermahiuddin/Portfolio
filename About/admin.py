from django.contrib import admin
from .models import Isavailable,AuthorPeronal,Boxes,Skills,Expreance,Education,CvUpload


# Register your models here.
class CvAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'mycv'
    ]


admin.site.register(Isavailable)
admin.site.register(AuthorPeronal)


admin.site.register(CvUpload,CvAdmin)

admin.site.register(Boxes)
admin.site.register(Skills)
admin.site.register(Expreance)
admin.site.register(Education)
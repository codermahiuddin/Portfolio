from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Portfolio,MultipleImageUpload
# Register your models here.

class MultipleImageUploadInline(admin.TabularInline):
    model = MultipleImageUpload
    extra = 2

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [MultipleImageUploadInline, ]

admin.site.register(Portfolio,PortfolioAdmin)



# class ImageAdmin(admin.StackedInline):
#     model = MultipleImageUpload

# # admin.site.register(Portfolio)
# @admin.register(Portfolio)

# class PortfolioAdmin(admin.ModelAdmin):
#     inlines = [ImageAdmin]

#     class Meta:
#         model = Portfolio

# # admin.site.register(MultipleImageUpload)
# @admin.register(MultipleImageUpload)

# class MultipleImageUploadAdmin(admin.ModelAdmin):
#     pass



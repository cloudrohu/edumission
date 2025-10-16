from django.contrib import admin
import admin_thumbnails
from django.utils.html import format_html
from .models import *
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    list_display = ['id']
    model = Images
    readonly_fields = ('id',)
    extra = 1


@admin_thumbnails.thumbnail('image')
class ProjectImageInline(admin.TabularInline):
    list_display = ['id']
    model = Project_Images
    readonly_fields = ('id',)
    extra = 1


@admin_thumbnails.thumbnail('image')
class ServiceImageInline(admin.TabularInline):
    list_display = ['id']
    model = Service_Images
    readonly_fields = ('id',)
    extra = 1

class Service_Key_FeatureInline(admin.StackedInline):
    model = Service_Key_Feature
    extra = 1
    fields = ('title', 'description', 'icon', 'icon_preview')
    readonly_fields = ('icon_preview',)

    def icon_preview(self, obj):
        if obj.icon:
            return format_html(f'<i class="{obj.icon}" style="font-size:22px;"></i>')
        return "-"
    icon_preview.short_description = "Preview"

    class Media:
        js = ('admin/js/icon-preview.js',)
        css = {
            'all': ('admin/css/icon-inline.css',)  # 👈 Custom styling
        }




class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','image_tag','featured_project', 'Top_Deals_Of_The_Day','Top_Selling_Products','Recommended_For_You', 'slug', 'create_at','update_at',]
    list_editable = ['featured_project', 'Top_Deals_Of_The_Day','Top_Selling_Products','Recommended_For_You']
    inlines = [ProductImageInline,]


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','title','image_tag', 'Project_Type','featured_project',  'slug', 'create_at','update_at',]
    list_editable = ['featured_project','Project_Type',]
    inlines = [ProjectImageInline,]



class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id','title','image_tag','featured_project',  'slug', 'create_at','update_at',]
    list_editable = ['featured_project',]
    inlines = [ServiceImageInline,Service_Key_FeatureInline]

admin.site.register(Service,ServiceAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images)
admin.site.register(Project_Images)
admin.site.register(Service_Images)
admin.site.register(Comment)




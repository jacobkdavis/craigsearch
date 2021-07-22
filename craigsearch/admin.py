from django.contrib import admin

from .models import SearchArea, SearchQuery



import django.contrib.admin.options as admin_opt

def duplicate_record(modeladmin:admin_opt.ModelAdmin, request, queryset):
    for object in queryset:
        from_id = object.id
        object.id = None
        object.save()
        message="dup from {} to {}".format(from_id, object.id)
        modeladmin.log_addition(request=request,object=object,message=message)

duplicate_record.short_description = "Duplicate Records"

class SearchQueryAdmin(admin.ModelAdmin):
    actions = [duplicate_record]


admin.site.register(SearchQuery, SearchQueryAdmin)


class SearchAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'areas')
    ordering = ['name']

admin.site.register(SearchArea, SearchAreaAdmin)

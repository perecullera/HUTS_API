from django.contrib import admin
from .models import Hut
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin





# Register your models here.

class HutResource(resources.ModelResource):

    class Meta:
        model = Hut



class HutAdmin(ImportExportActionModelAdmin):
    resource_class = HutResource
    pass

# class HutAdmin(ImportExportModelAdmin):
#     resource_class = HutResource
#     pass

admin.site.register(Hut,HutAdmin)




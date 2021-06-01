from django.contrib import admin
from .models import AdminFileLog
from django.urls import reverse
from django.template.response import TemplateResponse


# Register your models here.

class AdminFileLogAdmin(admin.ModelAdmin):

    verbose_name = "Upload and Replace new batch of data"
    verbose_name_plural =  "Upload and Replace new batch of data"
    def has_add_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):

        context = dict(
           # Include common variables for rendering the admin template.
           self.admin_site.each_context(request)
        )
        return TemplateResponse(request, 'file_upload.html', context)
        pass

admin.site.register(AdminFileLog, AdminFileLogAdmin)

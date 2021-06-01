from django.contrib import admin
from django.forms import ModelForm
from .models import AdminFileLog
from django.urls import reverse
from django.template.response import TemplateResponse


# Register your models here.

class AdminFileLogAdmin(admin.ModelAdmin):

    class Media:
        js = ['file_upload.js']

    def has_add_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):

        context = self.admin_site.each_context(request)
        print(context);
        context["title"] = "Upload new file"
        return TemplateResponse(request, 'file_upload.html', context)
        pass

admin.site.register(AdminFileLog, AdminFileLogAdmin)

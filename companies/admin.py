from django.contrib import admin

from companies.models import JobApplication


# Register your models here.
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job','member','applied_at','status')
    # search_fields = ('name',)
    list_filter = ('job','status')
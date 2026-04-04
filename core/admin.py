from django.contrib import admin

from core.base_admin import BaseTabularInline, BaseModelAdmin
from core.models import Skill, SkillCategory


# Register your models here.


class SkillInline(BaseTabularInline):
    model = Skill
    extra = 1
    fields = ('name',)


@admin.register(SkillCategory)
class SkillCategoryAdmin(BaseModelAdmin):
    list_display = ('name','icon')
    search_fields = ('name',)
    inlines = [SkillInline]  #


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name','category','is_verified')
    search_fields = ('name',)
    list_filter = ('category','is_verified')

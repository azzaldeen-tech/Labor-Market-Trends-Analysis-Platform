from django.contrib import admin

from core.base_admin import BaseTabularInline, BaseModelAdmin
from core.models import Skill, SkillCategory, City, Region, Country


# Register your models here.

class RegionInline(BaseTabularInline):
    model = Region
    extra = 1
    fields = ('name', 'code')
class CityInline(BaseTabularInline):
    model = City
    extra = 1

@admin.register(Country)
class CountryAdmin(BaseModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name',)
    inlines = [RegionInline] # دمج المناطق داخل الدولة

@admin.register(Region)
class RegionAdmin(BaseModelAdmin):
    list_display = ('name', 'code', 'country')
    list_filter = ('country',) # يمكنك الفلترة حسب الدولة
    search_fields = ('name',)
    inlines = [CityInline] # إضافة المدن هنا لسهولة الإدخال

@admin.register(City)
class CityAdmin(BaseModelAdmin):
    list_display = ('name', 'region')
    list_filter = ('region__country', 'region') # فلترة هرمية (دولة ثم منطقة)
    search_fields = ('name',)



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

from django.conf import settings
from django.db import models


# import json
# from django.utils.translation import gettext_lazy as _



class SkillCategory(models.Model):
    """قطاعات العمل الكبرى (مثلاً: تكنولوجيا المعلومات، الهندسة)"""
    name = models.CharField(max_length=255, verbose_name="Category")
    # name_en = models.CharField(max_length=100, verbose_name="التصنيف بالإنجليزي")
    slug = models.SlugField(unique=True, help_text="Write the link in English here (e.g., web-development)")
    icon = models.CharField(max_length=50,null=True, blank=True, help_text="FontAwesome icon class")

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name_en)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Skill(models.Model):

    # class SkillType(models.TextChoices):
    #     TECH = 'tech', _('Hard Skill')
    #     SOFT = 'soft', _('Soft Skill')
    #     TOOL = 'tool', _('Tool')

    suggested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=100, unique=True)
    is_verified = models.BooleanField(default=True, verbose_name="موثقة من الآدمن")


    def __str__(self):
        return self.name



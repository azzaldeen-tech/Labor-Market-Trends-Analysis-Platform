from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser
from config import settings


# Create your models here.
class MemberProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='member_profile',
        verbose_name=_("User Account")
    )

    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avater = models.ImageField(
        _("Avater"),
        upload_to='members/avaters/',
        null=True,
        blank=True,
        help_text=_("Preferably 512x512 pixels")
    )

    def __str__(self):
        return self.name

    @property
    def name(self):
        # عندما يستدعي الكود .name للعضو، ندمج الاسمين
        return f"{self.first_name or ''} {self.last_name or ''}".strip()  or self.user.username


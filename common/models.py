from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Sponsor(BaseModel):
    name = models.CharField(_("Name"),max_length=255)
    logo = models.ImageField(_("Logo"),upload_to="sponsors")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Sponsor")
        verbose_name_plural = _("Sponsors")

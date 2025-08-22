from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Product(BaseModel):
    name = models.CharField(_("Name"),max_length=255)
    description = models.TextField(_("Description"))
    price = models.DecimalField(_("Price"),max_digits=10, decimal_places=2)
    image = models.ImageField(_("Image"),upload_to="products")
    category = models.ForeignKey(
        "products.ProductCategory", on_delete=models.RESTRICT, related_name="products",verbose_name=_("Category"),
    )
    is_featured = models.BooleanField(_("Is Featured"),default=False)
    created_at = models.DateTimeField(_("Created At"),auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductVariant(BaseModel):
    product = models.ForeignKey(
        "products.Product", on_delete=models.RESTRICT, related_name="variants",verbose_name=_("Product"),
    )
    name = models.CharField(_("Name"),max_length=255)
    price = models.DecimalField(_("Price"),max_digits=10, decimal_places=2)
    color = models.CharField(_("Color"),max_length=255, null=True, blank=True)
    size = models.CharField(_("Size"),max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.color} - {self.size}"

    class Meta:
        verbose_name = _("Product Variant")
        verbose_name_plural = _("Product Variants")


class ProductCategory(BaseModel):
    name = models.CharField(_("Name"),max_length=30, unique=True)
    description = models.CharField(_("Description"),max_length=500, blank=True)
    image = models.ImageField(_("Image"),upload_to="categories/", blank=True, null=True)
    is_active = models.BooleanField(_("Is Active"),default=True)
    sort_order = models.PositiveSmallIntegerField(_("Sort Order"),default=0)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name

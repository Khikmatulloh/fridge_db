from modeltranslation.translator import register, TranslationOptions
from .models import Product, ProductCategory, ProductVariant


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("name", "description",)


@register(ProductVariant)
class ProductVariantTranslationOptions(TranslationOptions):
    fields = ("name", "color", "size",)


@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ("name", "description",)

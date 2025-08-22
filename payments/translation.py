from modeltranslation.translator import register, TranslationOptions
from .models import Provider, Discount, Promocode


@register(Provider)
class ProviderTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Discount)
class DiscountTranslationOptions(TranslationOptions):
    fields = ("name", "description",)


@register(Promocode)
class PromocodeTranslationOptions(TranslationOptions):
    fields = ("description",)

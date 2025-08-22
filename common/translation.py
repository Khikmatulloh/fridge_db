from modeltranslation.translator import register, TranslationOptions
from .models import Sponsor


@register(Sponsor)
class SponsorTranslationOptions(TranslationOptions):
    fields = ("name",)

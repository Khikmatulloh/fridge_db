from modeltranslation.translator import register, TranslationOptions
from .models import Profession, UserFeedback


@register(Profession)
class ProfessionTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(UserFeedback)
class UserFeedbackTranslationOptions(TranslationOptions):
    fields = ("message",)

from modeltranslation.translator import register, TranslationOptions
from .models import BlogPost, BlogCategory, Tag, Comment


@register(BlogPost)
class BlogPostTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(BlogCategory)
class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ("text",)

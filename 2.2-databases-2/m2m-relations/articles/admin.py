from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


class ArticleScopeFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            forms_dict = form.cleaned_data
            if forms_dict.get("is_main"):
                main_count += 1
            if main_count > 1:
                raise ValidationError("У статьи может быть только 1 основной раздел")
        if main_count == 0:
            raise ValidationError("У статьи должен быть хотя бы 1 основной раздел")
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    extra = 5
    formset = ArticleScopeFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]


@admin.register(Scope)
class ArticleAdmin(admin.ModelAdmin):
    pass
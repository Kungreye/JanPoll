# _*_ coding: utf-8 _*_

from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # the first element of each tuple is the title of the fieldset.
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}), # `collapse` field will hide.
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

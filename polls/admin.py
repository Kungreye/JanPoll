# _*_ coding: utf-8 _*_

from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # the first element of each tuple is the title of the fieldset.
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}), # `collapse` field will hide.
    ]

    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']   # `LIKE` query behind the scenes


admin.site.register(Question, QuestionAdmin)

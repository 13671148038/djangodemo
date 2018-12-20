from django.contrib import admin
from .models import Question, Choice


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    list_display = ('pub_date', 'question_text')


class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('baseInfo', {'fields': ['choice_text', 'question_id']}),
        ('time', {'fields': ['votes']})
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

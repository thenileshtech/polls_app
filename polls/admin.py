from django.contrib import admin

# Register your models here.

from .models import Question,Choice

class ChoiceInline(admin.StackedInline):
    model=Choice
    extra=2
class PollsAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,{'fields':['question_text']}),
        ('Date Information',{'fields':['pub_date']},)
    ]
    inlines=[ChoiceInline]
    # wpr="No"
    # if 'was_published_recently'==True:
    #     wpr="Yes"
    list_display=['question_text','pub_date','was_published_recently']

    list_filter=['pub_date']
    search_fields=['question_text']

admin.site.register(Question,PollsAdmin)
# admin.site.register(Choice)
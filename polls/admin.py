from django.contrib import admin
from polls.models import Question,Choice

# Register your models here.
class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3
class QuestionAdmin(admin.ModelAdmin):
	list_display=('question_text','pub_date','was_published_recently')
	list_filter = ['pub_date']
	fieldsets = [
		(None,{'fields':['question_text']}),
		
		('Data information',{'fields':['pub_date']}),
	]
	inlines=[ChoiceInLine]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
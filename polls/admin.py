from django.contrib import admin
from polls.models import Question,Choice

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,{'fields':['question_text']}),
		# ('Choice',{'field':['choice_text']}),
		('Data information',{'fields':['pub_date']}),
	]
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
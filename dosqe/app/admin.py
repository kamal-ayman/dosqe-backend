from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(School)
admin.site.register(Servant)
admin.site.register(Served)
admin.site.register(ServedPresence)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(QuizFillEmpty)
admin.site.register(QuizFillEmptyOption)
admin.site.register(QuizFillEmptyOptionAnser)
admin.site.register(QuizChoose)
admin.site.register(QuizChooseOption)
admin.site.register(QuizChooseAnser)
admin.site.register(QuizVoice)
admin.site.register(QuizVoiceAnser)



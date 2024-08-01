from django.contrib import admin
from .models import Quiz, Question, Answer, UserQuizProgress, UserAnswer, Options

# Register your models here.


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'quiz_title', 'quiz_desc']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'quiz', 'question_text']


@admin.register(Options)
class OptionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'option_text']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'answer', 'is_correct']


@admin.register(UserQuizProgress)
class UserQuizProgressAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'quiz', 'score', 'completed']


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'question', 'answer', 'is_correct']

from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cate_title', 'created_by']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_title', 'created_by', 'category', 'price']


# vidoe
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']


# pdf
@admin.register(PDF)
class PDFAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']

# quiz


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'course']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_text', 'quiz']


@admin.register(Options)
class OptionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'options']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'question']


# student progress
@admin.register(StudentProgress)
class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ['student', 'quiz', 'question',
                    'selected_option', 'is_correct', 'attempted_at'
                    ]
    list_filter = ['quiz']
    search_fields = [
        'student__username', 'quiz__title',
        'question__question_text'
    ]

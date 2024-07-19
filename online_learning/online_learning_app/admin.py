from django.contrib import admin
from .models import Category, Course, PDF, Video, Quiz, Question, Answer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cate_title', 'created_by']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_title', 'created_by', 'category', 'price']


@admin.register(PDF)
class PDFAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'quiz']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'question', 'is_correct']

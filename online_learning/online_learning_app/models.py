from django.db import models
from django.utils import timezone
from accounts.models import CustomUserModel
# Category


class Category(models.Model):
    '''
    this model is responsible for creating category
    '''
    cate_title = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.cate_title

# Course


class Course(models.Model):
    created_by = models.CharField(max_length=200)
    course_image = models.ImageField(upload_to='course_image/')
    course_title = models.CharField(max_length=200)
    course_desc = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.course_title

# PDF Model


class PDF(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='pdfs')
    pdf_file = models.FileField(upload_to='course_pdfs/')
    title = models.CharField(max_length=200)
    pdf_des = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.title

#  video Model


class Video(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='videos')
    video_file = models.FileField(upload_to='course_videos/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# Quize Model


class Quiz(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='questions'
    )
    question_text = models.TextField()

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text


class Options(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='options')
    options = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.options


class StudentProgress(models.Model):
    student = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(
        Options, on_delete=models.CASCADE, null=True
    )
    is_correct = models.BooleanField(default=False)
    attempted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.student} - {self.quiz} - {self.question}'

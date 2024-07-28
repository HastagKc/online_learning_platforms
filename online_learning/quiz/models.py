from django.db import models
from accounts.models import CustomUserModel
from online_learning_app.models import *
from django.utils import timezone


# Create your models here.
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
        Question, on_delete=models.CASCADE, related_name='options'
    )
    options = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.options


class StudentProgress(models.Model):
    student = models.ForeignKey(
        CustomUserModel, on_delete=models.CASCADE,
        related_name='student'
    )
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE,
        related_name='quiz'
    )
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='question')
    selected_option = models.ForeignKey(
        Options, on_delete=models.CASCADE, null=True)
    is_correct = models.BooleanField(default=False)
    attempted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.student} - {self.quiz} - {self.question}'

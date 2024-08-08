from django.db import models
from online_learning_app.models import Course

# Create your models here.

# quiz


class Quiz(models.Model):
    course = models.ForeignKey(
        Course, related_name='quizes', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# question


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text

# answer

# Answer Model


class Answer(models.Model):
    question = models.OneToOneField(
        Question, related_name='correct_answer', on_delete=models.CASCADE
    )
    answer_text = models.CharField(max_length=200)

    def __str__(self):
        return f"Correct Answer for: {self.question.question_text}"


# option

class Option(models.Model):
    question = models.ForeignKey(
        Question, related_name='options', on_delete=models.CASCADE
    )
    option_text = models.CharField(max_length=255)

    def __str__(self):
        return self.option_text

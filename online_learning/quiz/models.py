from django.db import models
from online_learning_app.models import Course

from accounts.models import CustomUserModel

# Create your models here.
# quiz model


class Quiz(models.Model):
    course = models.ForeignKey(
        Course, related_name='quiz', on_delete=models.CASCADE
    )
    quiz_title = models.CharField(max_length=200)
    quiz_desc = models.CharField(max_length=200)

    def __str__(self):
        return self.quiz_title


# question model
class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, related_name='questions', on_delete=models.CASCADE
    )
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


# options model
class Options(models.Model):
    question = models.ForeignKey(
        Question, related_name='options', on_delete=models.CASCADE
    )
    option_text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.question} - {self.option_text}'


# answer model


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.CASCADE
    )
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.answer


# progress model
class UserQuizProgress(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.quiz.quiz_title} - {self.score}'


class UserAnswer(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Options, on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    def __str__(self):
        return f'{self.user.username} - {self.question.question_text} - {self.answer.option_text} - {"Correct" if self.is_correct else "Incorrect"}'

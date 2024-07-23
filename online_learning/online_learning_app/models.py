from django.db import models

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

    def __str__(self):
        return self.title

# Question Model


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()

    def __str__(self):
        return self.question_text

# Answer


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

from .models import Question, Answer
from .models import Video, Course
from django import forms
from .models import Category, Course, PDF, Video, Quiz


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cate_title']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'course_image', 'course_title',
            'course_desc', 'category', 'price'
        ]


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['course', 'video_file', 'title']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(VideoForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['course'].queryset = Course.objects.filter(
                created_by=user.username
            )


class PDFForm(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ['course', 'pdf_file', 'title', 'pdf_des']

# quiz


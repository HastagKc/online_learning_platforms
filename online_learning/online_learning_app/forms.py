from .models import Video, Course
from django import forms
from .models import Category, Course, PDF, Video


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cate_title']
        widgets = {
            'cate_title': forms.TextInput(attrs={
                'class': 'form-control',
            })
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'course_image', 'course_title',
            'course_desc', 'category', 'price'
        ]
        widgets = {
            'course_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'course_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Title'}),
            'course_desc': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Course Description'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
        }


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['course', 'video_file', 'title']
        widgets = {
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Name'}),
            'video_file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Video Title'}),
        }

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
        widgets = {
            'pdf_file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course title',
            }),
            'pdf_des': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course description'
            }),
        }

# quiz

from django import forms
from .models import Quiz, Question, Options, Answer, UserQuizProgress, UserAnswer


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['quiz_title', 'quiz_desc']
        widgets = {
            'quiz_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quiz Title'}),
            'quiz_desc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quiz Description'}),
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['quiz', 'question_text']
        widgets = {
            'quiz': forms.Select(attrs={'class': 'form-control'}),
            'question_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Question Text'}),
        }


class OptionsForm(forms.ModelForm):
    class Meta:
        model = Options
        fields = ['question', 'option_text']
        widgets = {
            'question': forms.Select(attrs={'class': 'form-control'}),
            'option_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option Text'}),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question', 'answer']
        widgets = {
            'question': forms.Select(attrs={'class': 'form-control'}),
            'answer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Answer Text'}),
        }


class UserQuizProgressForm(forms.ModelForm):
    class Meta:
        model = UserQuizProgress
        fields = ['user', 'quiz', 'score', 'completed']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'quiz': forms.Select(attrs={'class': 'form-control'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Score'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class UserAnswerForm(forms.ModelForm):
    class Meta:
        model = UserAnswer
        fields = ['user', 'question', 'answer', 'is_correct']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'question': forms.Select(attrs={'class': 'form-control'}),
            'answer': forms.Select(attrs={'class': 'form-control'}),
            'is_correct': forms.Select(choices=[(True, 'Correct'), (False, 'Incorrect')], attrs={'class': 'form-control'}),
        }

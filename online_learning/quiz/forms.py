from django.forms import inlineformset_factory
from django import forms
from .models import Quiz, Question, Answer, Option


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['course_title', 'title', 'description']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['quiz', 'question_text']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question', 'answer_text']


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['question', 'option_text', 'is_correct']


OptionFormSet = inlineformset_factory(
    Question,
    Option,
    form=OptionForm,
    extra=4  # Number of forms to display
)

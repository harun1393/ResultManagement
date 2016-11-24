from django import forms
from teachers.models import ClassManagement
from .models import ResultsInfo

class BaseResultForm(forms.Form):
    DEPT = (
        ('cse', 'CSE'),
        ('bba', 'BBA'),
    )
    department = forms.ChoiceField(choices=DEPT, widget=forms.Select(attrs={'class':''}))
    #exam_code = forms.ModelChoiceField(queryset=ExamInfo.objects.all(), widget=forms.Select(attrs={'class': ''}))
    semester = forms.IntegerField(widget=forms.NumberInput(attrs={'class':''}))


# Django form to get published result for student
class ResultForm(BaseResultForm):
    student_id = forms.IntegerField(widget=forms.NumberInput(attrs={'class':''}))
    semester = forms.IntegerField(widget=forms.NumberInput(attrs={'class':''}))
    EXAMS = (
        ('mid', 'Mid Term'),
        ('final', 'Final'),
    )
    exam = forms.ChoiceField(choices=EXAMS, widget=forms.Select(attrs={'class':''}))


# Submit result from teacher
class AddResultForm(forms.ModelForm):
    class Meta:
        model = ResultsInfo
        fields = '__all__'
        exclude = ('id',)


# Generate result to csv
class GenerateResultForm(BaseResultForm):
    batch = forms.IntegerField()





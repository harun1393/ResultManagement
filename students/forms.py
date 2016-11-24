from django import forms
from .models import StudentsInfo

class AddNewStudentForm(forms.ModelForm):
    student_id = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    batch = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    department = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    section = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = StudentsInfo
        fields = ['student_id', 'name', 'batch', 'department', 'section']

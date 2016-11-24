from django import forms
from .models import TeachersInfo


class AddTeacherForm(forms.ModelForm):
    class Meta:
        model = TeachersInfo
        fields = ('teacher_code','teacher_name','email','password',)




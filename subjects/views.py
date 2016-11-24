from django.shortcuts import render
from teachers.models import ClassManagement
from .models import SubjectsInfo


# Logged in teachers associated subject list
def my_subjects(request):
    user = request.user.id
    subjects = ClassManagement.objects.filter(teacher=user)
    context = {'subjects': subjects, 'user': user}
    return render(request, 'subjects/my-subjects.html', context)


# All Subject list
def all_subjects(request):
    subjects = SubjectsInfo.objects.all()
    context = {'subjects': subjects}
    return render(request, 'subjects/all-subjects.html', context)
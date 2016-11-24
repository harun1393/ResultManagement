from django.shortcuts import render
from .models import StudentsInfo
from .forms import AddNewStudentForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def all_students(request):
    user = request.user
    students = StudentsInfo.objects.all()
    context = {'students': students, 'user':user}
    return render(request, 'students/student-list.html', context)


def add_students(request):
    form = AddNewStudentForm()
    if request.method == 'POST':
        form = AddNewStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students-list'))
    context = {'form':form}
    return render(request, 'students/add-students.html',context)

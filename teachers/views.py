from django.shortcuts import render
from subjects.models import SubjectsInfo
from django.contrib.auth.decorators import login_required
from students.models import StudentsInfo
from .models import ClassManagement, TeachersInfo
from .forms import AddTeacherForm
import hashlib
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse



@login_required(login_url='login')
def admin_panel(request):
    user = request.user
    subjects = ClassManagement.objects.filter(teacher=user.id)
    context = {'subjects':subjects, 'user':user}
    return render(request, 'teachers/panel-home.html',context)


def class_management(request):
    user = request.user
    classes = ClassManagement.objects.all()
    context = {'classes': classes,'user':user}
    return render(request, 'teachers/class-manage.html', context)


# Add new teacher
def add_teacher(request):
    form = AddTeacherForm()
    if request.method == 'POST':
        form = AddTeacherForm(request.POST)
        if form.is_valid():
            teacher=form.save(commit=False)
            formPass = form.cleaned_data['password']
            passWord = hashlib.md5(formPass).hexdigest()
            print passWord
            teacher.password = passWord
            teacher.is_active =1
            teacher.is_superuser = 0
            teacher.save()
            return HttpResponseRedirect(reverse('teachers-list'))
    context = {'form': form}
    return render(request, 'teachers/add-teacher.html', context)


def teachers_list(request):
    teachers = TeachersInfo.objects.all()
    context = {'teachers': teachers}
    return render(request, 'teachers/teachers-list.html', context)


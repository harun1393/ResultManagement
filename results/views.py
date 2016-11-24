from django.shortcuts import render
from .forms import AddResultForm, ResultForm
from django.db import connection
from .models import ResultsInfo
from students.models import StudentsInfo
from subjects.models import SubjectsInfo
from django.db import connection
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def gpa_calculator(marks):
    if marks >=80:
        gpa = 4
    elif marks >= 75 <= 79:
        gpa = 3.75
    elif marks >= 70 <= 74:
        gpa = 3.50
    elif marks >= 65 <= 69:
        gpa = 3.25
    elif marks >= 60 <= 64:
        gpa = 3.00
    elif marks >= 55 <= 59:
        gpa = 2.75
    elif marks >= 50 <= 54:
        gpa = 2.50
    elif marks >= 45 <= 49:
        gpa = 2.25
    elif marks >= 40 <= 44:
        gpa = 2.00
    elif marks <= 39:
        gpa = 0.00
    return gpa


# Student part to see published result
def results(request):
    form = ResultForm()
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            st_id = form.cleaned_data['student_id']
            semester = form.cleaned_data['semester']
            dept = form.cleaned_data['department']
            exam = form.cleaned_data['exam']
            result = ResultsInfo.objects.filter(student_id=st_id,semester=semester, department=dept)
            print result
            if result:
                sum_gpa = 0
                sum_credit=0
                for sub in result:
                    # SGPA Calculation rules
                    # Sum(credit *point )/Sum(credit)
                    if exam == 'final':
                        # for mid term result
                        s = sub.subject_id.credit * gpa_calculator(sub.final_number)
                        sum_gpa = sum_gpa + s
                        sum_credit = sum_credit+sub.subject_id.credit
                    else:
                        # for Final exam result
                        s = sub.subject_id.credit * gpa_calculator(sub.mid_number)
                        sum_gpa = sum_gpa + s
                        sum_credit = sum_credit + sub.subject_id.credit
                sgpa = sum_gpa/sum_credit
                student = StudentsInfo.objects.get(student_id=st_id)
                context = {'results': result, 'student':student, 'exam':exam, 'sgpa': sgpa, 'totalCredit': sum_credit}
                return render(request, 'results/markshit.html', context)
            else:
                context = {'errMsg': "Result not found !!",'form': form}
                return render(request, 'results/results.html', context)
        else:
            pass
    context = {'form': form}
    return render(request, 'results/results.html', context)


# A form to add new result
def add_result(request):
    form = AddResultForm()
    if request.method == 'POST':
        form = AddResultForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            studentId = form.cleaned_data['student_id']
            subjectId = form.cleaned_data['subject_id']
            semester = form.cleaned_data['semester']
            mid = form.cleaned_data['mid_number']
            final = form.cleaned_data['final_number']

            result,trueOrFalse = ResultsInfo.objects.get_or_create(student_id=studentId, subject_id=subjectId, semester=semester)
            if result:
                print "result found"
                if final == None:
                    print "in final"
                    result.mid_number = mid
                    result.save()
                else:
                    print "in mid"
                    result.final_number = final
                    result.save()
            return HttpResponseRedirect(reverse('admin-panel'))

    context = {'form': form,}
    return render(request, 'results/add-result.html', context)
'''
# Add marks form route
def add_marks(request):
    if request.method == 'POST':
        form_data = request.POST.getlist('stdId')
        department = request.POST.get('department')
        semester = request.POST.get('semester')
        batch = request.POST.get('batch')
        section = request.POST.get('section')
        examCode = request.POST.get('examCode')
        subject = request.POST.get('subject')
        #examId= ExamInfo.objects.get(exam_name=examCode)
        students = StudentsInfo.objects.filter(department=department, batch=batch, section=section)
        for stdID, marks in zip(students,form_data):
            markshit = ResultsInfo(student_id=stdID.student_id, subject_code=subject, semester=semester, dept=department, exam_id=examId, marks=marks )
            markshit.save()
        context = {}
        return render(request,'teachers/result-confirm.html', context)

# All exam info
def all_exams(request):
    exams = ExamInfo.objects.all()
    context = {'exams': exams}
    return render(request, 'results/all-exams.html', context)


# Generate all result to csv for superuser
@login_required(login_url='login')
def generate_result(request):
    user = request.user
    if not user.is_superuser:
        logout(request)
        return HttpResponseRedirect(reverse('login'))
    else:
        form = GenerateResultForm()
        if request.method == 'POST':
            form = GenerateResultForm(request.POST)
            if form.is_valid():
                department = form.cleaned_data['department']
                semester = form.cleaned_data['semester']
                batch = form.cleaned_data['batch']
                examCode = form.cleaned_data['exam_code']
                examId = ExamInfo.objects.get(exam_name=examCode)
                result = ResultsInfo.objects.filter(dept=department, exam_id=examId.id, semester=semester, batch=batch )
                if result:
                    subjects = SubjectsInfo.objects.filter(semester= semester)
                    context = {'result': result, 'subjects':subjects}
                    return render(request, 'results/generate-markshit.html', context)
        context = {'form': form}
        return render(request,'results/generate-results.html', context)'''

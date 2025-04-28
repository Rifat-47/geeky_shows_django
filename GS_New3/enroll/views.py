from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import User
from .forms import StudentRegistration, TeacherRegistration
from django.db.models import Max
# Create your views here.

def studentinfo(request, stu_id=None):
    if stu_id is None:
        stud = User.objects.all()
        return render(request, 'enroll/studetails.html', {'stu': stud, 'is_single_student': False})
    else:
        stud = get_object_or_404(User, pk=stu_id)
        return render(request, 'enroll/studetails.html', {'stu': [stud], 'is_single_student': True})


def thankyou(request):
    return render(request, 'enroll/success.html')

def showformdata(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        print(request.POST.get('name'))
        if fm.is_valid():
            print('-----------')
            print(request.POST)
            print('-----------')
            # fm = StudentRegistration()
            student_name = fm.cleaned_data['stuname']
            email = fm.cleaned_data['stuemail']
            password = fm.cleaned_data['stupass']

            reg = User(student_name= student_name, email=email, password=password)
            reg.save()
            return HttpResponseRedirect('/enroll/success')
        else:
            print('data not valid')
            fm = StudentRegistration(request.POST)
    else:
        fm = StudentRegistration(auto_id= 'id_for_%s', label_suffix=': ')
        fm.order_fields(field_order= ['student_name', 'email', 'password'])
    return render(request, 'enroll/userregistration.html', {'form': fm})

def teacher_form(request):
    if request.method == "POST":
        fm = TeacherRegistration(request.POST)
        if fm.is_valid():
            teacher_name = fm.cleaned_data['teacher_name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            user = User(teacher_name=teacher_name, email=email, password=password)
            user.save()
            return HttpResponseRedirect('/enroll/success')
    else:
        fm = TeacherRegistration(auto_id= 'id_for_%s', label_suffix=': ')
    return render(request, 'enroll/teacherregistration.html', {'form': fm})

def student_form(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            student_name = fm.cleaned_data['student_name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            user = User(student_name=student_name, email=email, password=password)
            user.save()
            return HttpResponseRedirect('/enroll/success')
    else:
        fm = StudentRegistration(auto_id= 'id_for_%s', label_suffix=': ')
    return render(request, 'enroll/studentregistration.html', {'form': fm})

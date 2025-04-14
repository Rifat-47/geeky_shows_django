from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Student
from .forms import StudentRegistration
from django.db.models import Max
# Create your views here.

def studentinfo(request, stu_id=None):
    if stu_id is None:
        stud = Student.objects.all()
        return render(request, 'enroll/studetails.html', {'stu': stud, 'is_single_student': False})
    else:
        stud = get_object_or_404(Student, pk=stu_id)
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
            stuname = fm.cleaned_data['stuname']
            stuemail = fm.cleaned_data['stuemail']
            stupass = fm.cleaned_data['stupass']

            reg = Student(stuname=stuname, stuemail=stuemail, stupass=stupass)
            reg.save()
            return HttpResponseRedirect('/enroll/success')
        else:
            print('data not valid')
            fm = StudentRegistration(request.POST)
    else:
        fm = StudentRegistration(auto_id= 'id_for_%s', label_suffix=': ')
        fm.order_fields(field_order= ['stuemail', 'stuname', 'stupass'])
    return render(request, 'enroll/userregistration.html', {'form': fm})

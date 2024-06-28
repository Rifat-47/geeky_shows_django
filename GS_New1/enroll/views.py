from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Student
from .forms import StudentRegistration
from django.db.models import Max
# Create your views here.

def studentinfo(request):
    stud = Student.objects.all()
    # print('Myoutput', stud)
    return render(request, 'enroll/studetails.html', {'stu': stud})


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
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            passs = fm.cleaned_data['passs']

            # Get the highest stuid in the database
            max_stuid = Student.objects.aggregate(Max('stuid'))['stuid__max']
            if max_stuid is None:
                new_stuid = 1
            else:
                new_stuid = max_stuid + 1
            reg = Student(stuid=new_stuid, stuname=name, stuemail=email, stupass=passs)
            reg.save()
            return HttpResponseRedirect('/enroll/success')
        else:
            print('data not valid')
    else:
        fm = StudentRegistration(auto_id= 'id_for_%s', label_suffix=': ')
        fm.order_fields(field_order= ['email', 'name'])
    return render(request, 'enroll/userregistration.html', {'form': fm})
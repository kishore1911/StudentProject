from django.shortcuts import render
from StudentApp.models import Student,Student2

#Create your views here.
def studentview(request):
    studentlist = Student.objects.order_by('marks')		#def-order is ASC-order (DJ-ORM-code)
    dict1={'studentlist':studentlist}
    return render(request,'StudentApp/students.html',context=dict1);


def student_homepage(request):				#new
    #students= Student2.objects.all()
    #students=Student2.objects.filter(marks__lt=35)
    #students=Student2.objects.filter(name__startswith='A')
    #students=Student2.objects.all().order_by('marks')  #ASC
    students=Student2.objects.all().order_by('-marks')   #DESC
    return render(request, 'StudentApp/index.html', {'students':students})

from StudentApp import forms;
#Create your views here.
def studentinputview(request):
    formsObj=forms.StudentForm()
    dict1={'form1':formsObj}
    return render(request,'StudentApp/input.html',context=dict1)


import time;
from StudentApp import forms;
def studentinputverifyview(request):
    if request.method == 'POST':
        formsObj = forms.StudentForm(request.POST);
        if formsObj.is_valid():
            print('Form-Request validation success and printing data');
            time.sleep(5)
            print('Name:', formsObj.cleaned_data['name'])
            print('Marks:', formsObj.cleaned_data['marks'])
            formsObj = forms.StudentForm();     #empty-form
            dict1 = {'form1': formsObj,'msg':'Data Submitted successfully...(Enter another data)'}
    return render(request, 'StudentApp/input.html',context=dict1);

import time;
from django.shortcuts import render
from StudentApp.forms import StudentForm
#Create your views here>
def studentinputview2(request):
    sentdata=False;
    if request.method=='POST':
        formObj=StudentForm(request.POST)
        if formObj.is_valid():
            print('Form-Request-data Validation Success and printing data')
            time.sleep(5)
            print('Name:',formObj.cleaned_data['name'])
            print('Marks:',formObj.cleaned_data['marks'])
            sentdata=True;
            formObj = StudentForm();            #empty-form
            dict1 = {'form1': formObj, 'sentdata': sentdata}
            return render(request, 'StudentApp/thankyou.html', context=dict1);
    formObj=StudentForm();
    dict1={'form1': formObj}
    return render(request,'StudentApp/input2.html',context=dict1);







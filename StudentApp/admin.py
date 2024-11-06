
from django.contrib import admin
from StudentApp.models import Student,Student2
#Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']

class Student2Admin(admin.ModelAdmin):
    list_display=['rollno', 'name', 'dob','marks','email', 'phonenumber','address']

admin.site.register(Student,StudentAdmin);  #register takes only 2-args at a time
admin.site.register(Student2,Student2Admin);    #hence use 2 register() functions statements

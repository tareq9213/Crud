from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . import forms
from first_app.models import Student


def index(request):
    student = Student.objects.all()

    return render(request, 'index.html', {'student': student})


def student_form(request):
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')

    context = {'title': "StudentForm", 'student_form': form}
    return render(request, 'student_form.html', context)


def student_info(request, id):
    user = Student.objects.get(pk=id)
    print(user.id)
    return render(request, 'student_info.html', {'user': user})


def student_update(request, id):
    user = Student.objects.get(pk=id)
    form = forms.StudentForm(instance=user)
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return index(request)

    context = {'student_form': form}
    return render(request, 'student_update.html', context)


def student_delete(request,id):
    student = Student.objects.get(pk=id).delete()
    context = {'delete_message':"Delete Done"}
    return render(request,'student_delete.html',context)

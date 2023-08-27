from django.shortcuts import render,redirect,get_object_or_404

# User authentication start 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from django.contrib import messages

# models
from .models import *
from .forms import *


# Create your views here.
def loginUser(request):
    # prevent already loged in users from seing login page
   
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,'User succesfully logged in')
            return redirect('index')
        else:
            messages.error(request,'Invalid username or password')
    context = {}
    return render(request,'app/login/login.html', context)   


def logoutUser(request):
    logout(request)
    return redirect('login')



class IndexView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        context = {}
        return render(request, 'app/dashboard/index.html', context)


class ProgramsView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        context = {}
        return render(request, 'app/dashboard/programs.html', context)


class PlacementView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        context = {}
        return render(request, 'app/dashboard/placement.html', context)


class ShowCourseView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        courses = Course.objects.all()
        print(f"course {courses}")
        context = {'courses': courses}
        return render(request, 'app/dashboard/show_course.html', context)


class CreateCourseView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        form = CourseForm()
        context = {'forms': form}
        return render(request, 'app/dashboard/create_course.html', context)

    @method_decorator(login_required(login_url='login'))
    def post(self, request):
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course saved successfully.')
            return redirect('courses')
        else:
            error_message = 'Error saving course record. Please check the form:'
            for field, errors in form.errors.items():
                field_errors = ', '.join(errors)
                error_message += f"\n{field.capitalize()}: {field_errors}"
            messages.error(request, error_message)

        context = {'forms': form}
        return render(request, 'app/dashboard/create_course.html', context)


class EditCourseView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        form = CourseForm(instance=course)
        context = {'forms': form}
        return render(request, 'app/dashboard/create_course.html', context)

    @method_decorator(login_required(login_url='login'))
    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses')
        context = {'forms': form}
        return render(request, 'app/dashboard/create_course.html', context)

class DeleteCourseView(View):
    @method_decorator(login_required(login_url='login'))
    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return redirect('courses')



# PROGRAM VIEWS
# ----------------------------------------------------------------
class ShowProgramView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        programs = Program.objects.first()
        print(programs)
        context = {'programs': programs}

        return render(request, 'app/dashboard/show_programs.html', context)

class CreateProgramView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        form = ProgramForm()
        context = {'forms': form}
        return render(request, 'app/dashboard/create-program.html', context)

    @method_decorator(login_required(login_url='login'))
    def post(self, request):
        form = ProgramForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Program saved successfully.')
            return redirect('programs')
        else:
            error_message = 'Error saving program record. Please check the form:'
            for field, errors in form.errors.items():
                field_errors = ', '.join(errors)
                error_message += f"\n{field.capitalize()}: {field_errors}"
            messages.error(request, error_message)

        context = {'forms': form}
        return render(request, 'app/dashboard/create_program.html', context)

class EditProgramView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request, pk):
        program = get_object_or_404(Program, pk=pk)
        form = ProgramForm(instance=program)
        context = {'forms': form}
        return render(request, 'app/dashboard/create_program.html', context)

    @method_decorator(login_required(login_url='login'))
    def post(self, request, pk):
        program = get_object_or_404(Program, pk=pk)
        form = ProgramForm(request.POST, request.FILES, instance=program)
        if form.is_valid():
            form.save()
            return redirect('programs')
        context = {'forms': form}
        return render(request, 'app/dashboard/create_program.html', context)
    

class DeleteProgramView(View):
    @method_decorator(login_required(login_url='login'))
    def post(self, request, pk):
        program = get_object_or_404(Program, pk=pk)
        program.delete()
        return redirect('programs')

# GRADES VIEWS
# ----------------------------------------------------------------
class ShowGradesView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        grades = Grade.objects.all()
        context = {'grades': grades}
        return render(request, 'app/dashboard/show_grades.html', context)

class CreateGradeView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        form = GradeForm()
        context = {'forms': form}
        return render(request, 'app/dashboard/create_grade.html', context)

    @method_decorator(login_required(login_url='login'))
    def post(self, request):
        form = GradeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Grade saved successfully.')
            return redirect('grades')
        else:
            error_message = 'Error saving grade record. Please check the form:'
            for field, errors in form.errors.items():
                field_errors = ', '.join(errors)
                error_message += f"\n{field.capitalize()}: {field_errors}"
            messages.error(request, error_message)

        context = {'forms': form}
        return render(request, 'app/dashboard/create_grade.html', context)



class EditGradeView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request, pk):
        grade = get_object_or_404(Grade, pk=pk)
        form = GradeForm(instance=grade)
        context = {'forms': form}
        return render(request, 'app/dashboard/create_grade.html', context)

    @method_decorator(login_required(login_url='login'))
    def post(self, request, pk):
        grade = get_object_or_404(Grade, pk=pk)
        form = GradeForm(request.POST, request.FILES, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grades')
        context = {'forms': form}
        return render(request, 'app/dashboard/create_grade.html', context)

class DeleteGradeView(View):
    @method_decorator(login_required(login_url='login'))
    def post(self, request, pk):
        grade = get_object_or_404(Grade, pk=pk)
        grade.delete()
        return redirect('grades')




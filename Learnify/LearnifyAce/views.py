from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Course, generateStudentId, RegisteredCourse, Lessons
from django.utils import timezone 
from django.contrib.auth.decorators import login_required
from .forms import CourseForm, LessonsForm

# Create your views here.
def home(request):
    courses = Course.objects.filter(startDate__lte=timezone.now())
    context = {
        "courses": courses,
    }
    return render(request, 'home.html', context)

def contacts(request):
    return render(request, "contacts.html")

def staff(request):
    courses = Course.objects.all()
    context = {
        "courses": courses,
    }
    return render(request, "staff.html", context)

def delete_course(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return redirect("staff")

def edit_course(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, f'Course updated successfully')
            return redirect("staff")
        else:
            print(form.errors)
    else:
        form = CourseForm(instance=course)
    context = {
        "form": form,
        "course": course
    }
    return render(request, "edit_course.html", context)

def all_lessons(request):
    lessons = Lessons.objects.all()
    context = {
        "lessons": lessons,
    }
    return render(request, "all_lessons.html", context)

def delete_lesson(request, pk):
    lesson = Lessons.objects.get(pk=pk)
    lesson.delete()
    return redirect("all-lessons")

def edit_lesson(request, pk):
    lesson = Lessons.objects.get(pk=pk)
    if request.method == "POST":
        form = LessonsForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            messages.success(request, f'Lesson updated successfully')
            return redirect("all-lessons")
    else:
        form = LessonsForm(instance=lesson)
        context = {
            "form": form,
            "lesson": lesson
        }
    return render(request, "edit_lesson.html", context)



@login_required
def register_course(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == "POST":
        user = request.user
        studentId = generateStudentId()
        register = RegisteredCourse.objects.create(student=user, course=course, studentId=studentId)
        register.save()
        messages.info(request, f'You have successfully registered for {course.name}')
        return redirect("classroom", pk=course.pk)
    context = {
        "course": course,
    }
    return render(request, "register_course.html", context)

def classroom(request, pk):
    course = Course.objects.get(pk=pk)
    lessons = Lessons.objects.filter(course=course).all()
    context = {
        "course": course,
        "lessons": lessons,
    }
    return render(request, "classroom.html", context)

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email = email).exists():
                messages.error(request, f'email already exists')
                return redirect("register")
            elif User.objects.filter(username = username).exists():
                messages.error(request, f'username already exists')
                return redirect("register")
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                username=username, password=password1)
            user.save()
            return redirect("login")
    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.error(request, f'Invalid username or password')
            return redirect("login")
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect("home")

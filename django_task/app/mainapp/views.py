from django.shortcuts import get_object_or_404,render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from . models import Student

def index(request):
    return render(request,'Home.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print("User authenticated successfully")
            return redirect('details_view')
        else:
            messages.error(request, "Invalid username or password.")
            print("User authentication failed")
            return redirect('login_view')
    return render(request,"login.html")


def logout_view(request):
    return render(request,"logout.html",{})

def home(request):
    return render(request,"Home.html",{})

def registration_tailwebs(request):
    if request.method == "POST":
       name = request.POST.get('name')
       subject = request.POST.get('subject')
       marks = request.POST.get('marks')
       user = Student(name=name, subject=subject, marks=marks)
       user.save()
       return redirect('details_view')
    return render(request,"Registration.html",{})

def success_view(request):
    return render(request,"success.html")

def details_view(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request,"student_details.html",context)

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.subject = request.POST.get("subject")
        student.marks = request.POST.get("marks")
        student.save()
        return redirect("details_view")

    context = {"student": student}
    return render(request, "edit_student.html", context)

def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
    except Student.DoesNotExist:
        pass
    return redirect('details_view')
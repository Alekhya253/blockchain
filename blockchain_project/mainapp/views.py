from django.shortcuts import render

def main_home(request):
    return render(request,"main_home.html")

def loginpage(request):
    return render(request, 'loginpage.html')

def admin_login(request):
    # Add your admin login logic here
    return render(request, 'admin_login_template.html')

def student_login(request):
    # Add your student login logic here
    return render(request, 'student_login_template.html')



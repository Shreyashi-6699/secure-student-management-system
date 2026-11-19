
from django.shortcuts import render


def student_list(request):
    return render(request, "students/dashboard.html")
  

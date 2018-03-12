from django.shortcuts import render, redirect

def index(request):
	return render(request, 'html/index.html')

def student(request):
	return render(request, 'html/student.html')

def teacher(request):
	return render(request, 'html/teacher.html')

def creator(request):
	return render(request, 'html/creator.html')
from django.http import HttpResponse
from django.shortcuts import render

def some_text(request):
	return render(request, 'newsfeed.html', {})
	return HttpResponse("This is some text response!")

def multiply_numbers(request, num1, num2):
	return HttpResponse(str(int(num1) * int(num2)))

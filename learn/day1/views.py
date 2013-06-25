from django.http import HttpResponse

def some_text(request):
	return HttpResponse("This is some text response!")

def multiply_numbers(request, num1, num2):
	return HttpResponse(str(int(num1) * int(num2)))
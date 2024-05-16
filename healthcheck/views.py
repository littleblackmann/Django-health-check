from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def health_check(request):
	data = {'status' : 'ok'}
	return JsonResponse(data)

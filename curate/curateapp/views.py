from django.shortcuts import render
from curateapp.models import Source

def collection(request):
	collection_list = Source.objects.all()
	return render(request,'index.html', {"collection_list":collection_list})

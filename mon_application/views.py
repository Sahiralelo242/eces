from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import etudiant as et


def index(request):
	# return HttpResponse('<h1>Hello : Accueil</h1>')
	return render(request, 'mon_application/index.html')



def all_etudiant(request):

	etudiants = et.objects.all().order_by("Option")

	return render(request, 'mon_application/etudiants.html', {'etudiants':etudiants})


def etudiant(request, id):
	number = int(id)
	student = get_object_or_404(et, id=number)

	# return HttpResponse('<h1>Hello : Etudiant id('+str(id)+') </h1>')
	return render(request, 'mon_application/etudiant.html', {'student' : student})

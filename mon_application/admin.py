from django.contrib import admin
from . import models

class etudiantAdmin(admin.ModelAdmin):

	list_display=['Matricule','nom','prenom','date_de_naissance','sexe']
	search_fields=['Matricule','Option','date_de_naissance','sexe']
	list_filter=["Matricule","nom","prenom",'date_de_naissance','sexe']
	#fields=["nom","prenom","Matricule"]
	fieldsets=[
		('Son nom',{'fields':["nom",]}),
		('Son prenom',{'fields':["prenom",]}),
		('Sa date de naissance',{'fields':["date_de_naissance",]}),
		('Son Sexe',{'fields':["sexe",]}),
		('Son Matricule',{'fields':["Matricule",]}),
		('Son Option',{'fields':["Option",]}),
		('Son Adresse',{'fields':["adresse",]}),	
		('La photo',{'fields':["photo",]}),
	]
	

admin.site.register(models.etudiant,etudiantAdmin)

# admin.site.register(models.Language)






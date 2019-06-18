from django.db import models




class etudiant(models.Model):

	SEXE = (
		
		('H', 'Homme'),
		('F', 'Femme')
	)

	Option = (

		('IG1', 'IG1'),
		('IG2', 'IG2'),
		('IG3', 'IG3'),
		('MI1', 'MI1'),
		('MI2', 'MI2'),
		('MI3', 'MI3'),
		('TL1', 'TL1'),
		('TL2', 'TL2'),
		('TL3', 'TL3')
		
	
	)

	nom = models.CharField(max_length=50, help_text="Donnez un nom pour l'étudiant")

	prenom = models.CharField(max_length=50, help_text="Donnez un prenom pour l'étudiant")

	date_de_naissance = models.DateField()

	sexe = models.CharField(max_length=5, choices=SEXE)

	Matricule = models.CharField(max_length=50, help_text="Le matricule de l'étudiant")

	Option = models.CharField(max_length=4, choices=Option, default="IG2")

	adresse = models.CharField(max_length=100)

	photo = models.FileField(upload_to="identiter", help_text="Photo de l'étudiant")

	Description = models.TextField()

	def __str__(self):
		return self.Matricule + '-' + self.nom +'-'+self.prenom




# class Language(models.Model):

# 	Type_Language= (

# 		('Python', 'Python'),
# 		('Ruby', 'Ruby'),
# 		('C++', 'C++'),
# 		('C', 'C'),
# 		('Java', 'Java'),
# 		('javaScript', 'javaScript'),
# 		('Php', 'Php')
		

# 	)


# 	Type_Language= models.CharField(max_length=10, choices=Type_Language, help_text="Choisissez un Language pour l'étudiant")


# 	def __str__(self):
# 		return self.Type_Language


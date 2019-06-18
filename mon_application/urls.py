from django.urls import path
from django.conf import settings
from . import views 
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index, name="home"),
	path('all-etudiant/', views.all_etudiant, name="etudiants"),
	path('etudiant/<int:id>', views.etudiant, name="etudiant"),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include

admin.site.site_header ="ECES STUDENT"
admin.site.site_title='eces student'

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include('mon_application.urls')),
]

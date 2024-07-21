from django.contrib import admin, messages
from .models import Student, Book, IssueBook
# Register your models here.
admin.site.site_header = 'E-Libarary boshqaruvtizimi'
admin.site.site_title = 'E-Libarary boshqaruvtizimi'
admin.site.index_header = 'E-Libarary boshqaruvtizimi'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('hemis_id', 'full_name', 'JSHSHIR', 'passport')
    list_filter = ('course', 'region', 'speciality', 'form_of_education')
    search_fields = ('hemis_id', 'full_name', 'JSHSHIR', 'passport')
from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline, \
GenericTabularInline
from fullhistory.models import*
from schools.models import *

class Institution_Management_Admin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class Institution_Feature_Admin(admin.ModelAdmin):
    list_display = ['feature', 'active']
    search_fields = ['feature']

admin.site.register(Institution_Management, Institution_Management_Admin)
admin.site.register(Institution_Feature, Institution_Feature_Admin)
admin.site.register(Boundary_Type)
admin.site.register(Boundary_Category)
admin.site.register(Boundary)
admin.site.register(Institution_Category)
admin.site.register(Institution_address)
admin.site.register(Moi_Type)
admin.site.register(Institution)
admin.site.register(Communication)
admin.site.register(Child)
admin.site.register(Student)
admin.site.register(Staff_Qualifications)
admin.site.register(Staff_Type)
admin.site.register(Staff)

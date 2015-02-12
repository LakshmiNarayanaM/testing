from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline, \
GenericTabularInline
from fullhistory.models import*
from library.models import *

class LibraryUsersTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class LibraryUsersAdmin(admin.ModelAdmin):
    list_display = ['user','active']
    search_fields = ['user']

admin.site.register(LibraryUsersType, LibraryUsersTypeAdmin)
admin.site.register(LibraryUsers, LibraryUsersAdmin)
admin.site.register(BookCategory)
admin.site.register(Book)
admin.site.register(BooksCopies)
admin.site.register(Books_Borrowed)
admin.site.register(BookRequest)
admin.site.register(Fine)
admin.site.register(AdvanceBook)

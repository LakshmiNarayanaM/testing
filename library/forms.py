from django import forms
from django.forms import ModelForm
from library.models import *

class LoginForm(forms.Form):
        username = forms.CharField(label=(u'Enter your username '))
        password = forms.CharField(label=(u'Enter your Password '),widget=forms.PasswordInput(render_value=False))


def make_book_form(id):

    """ Create Book Form """
    book_cateory = forms.ModelChoiceField(label='Book Category',queryset=BookCategory.objects.filter(institution__id=int(id), active=2))
    class cust_book_form(ModelForm):
        """ Create Book Form """
        class Meta:
            model = Book
            fields=('book_category', 'title', 'author', 'publisher', 'keyword', 'isbn_code', 'year_of_pub', 'active')
            exclude = ['institution']

    return cust_book_form


class AdvanceBookForm(ModelForm):
    class Meta:
        model = AdvanceBook
        exclude = ['book','booked_by','active']

class BookCategoryForm(ModelForm):
    class Meta:
        model = BookCategory
        exclude = ['institution']
        fields = ('name','active')



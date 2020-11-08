from django import forms
from Books.models import Book
from django.forms import ModelForm

# class BookcreateForm(forms.Form):
#
#     book_name=forms.CharField(max_length=120)
#     author=forms.CharField(max_length=120)
#     price=forms.IntegerField()
#     pages=forms.IntegerField()

class BookForm(ModelForm):
    class Meta:
        model=Book
        fields="book_name","author","price","pages"

    def clean(self):
        cleaned_data=super().clean()
        bookname=cleaned_data.get("book_name")
        price=cleaned_data.get("price")
        pages=cleaned_data.get("pages")
        Books=Book.objects.filter(book_name=bookname)

        if(Books):
            msg="book with same name already exist"
            self.add_error("book_name",msg)
        if price<100:
            msg="please put the price greater than 100"
            self.add_error("price",msg)
        if pages<50:
            msg="page number should be greater than 50"
            self.add_error("pages",msg)

class BookUpdateForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"
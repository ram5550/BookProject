from django.shortcuts import render, redirect

from Books.models import Book
from Books.forms import BookForm,BookUpdateForm
from Books.models import Book
# Create your views here.


def bookCreate(request):
    template_name="bookcreate.html"
    context={}
    context["form"]=BookForm()
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            # book_name=form.cleaned_data.get("book_name")
            # author=form.cleaned_data.get("author")
            # price=form.cleaned_data.get("price")
            # pages=form.cleaned_data.get("pages")
            # obj=Book(book_name=book_name,author=author,price=price,pages=pages)
            # obj.save()
            form.save()
            return redirect("list")
        else:
            context["form"]=form
            return render(request, template_name, context)


    return render(request,template_name,context)

def listBook(request):
    template_name="list.html"
    qs=Book.objects.all()
    context={}
    context["books"]=qs
    return render(request,template_name,context)

def viewBook(request,pk):
    template_name="book.html"
    qs=Book.objects.get(id=pk)
    context={}
    context["book"]=qs
    return render(request,template_name,context)

def deleteBook(request,pk):
    qs=Book.objects.get(id=pk).delete()
    return redirect("list")

def updateBook(request,pk):
    Books=Book.objects.get(id=pk)
    form=BookUpdateForm(instance=Books)
    context={}
    context["form"]=form

    if request.method=="POST":
        form=BookUpdateForm(instance=Books,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")

    return render(request,"bookUpdate.html",context)
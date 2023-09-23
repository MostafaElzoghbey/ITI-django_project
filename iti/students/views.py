import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from .models import *
from authmansoura.models import *
from authmansoura.form import BorrowBookForm

# Create your views here.


def home(req):
    return render(req, 'index.html')


def mybooks(request):
    data = Book.objects.all()
    context = {
        'data': data
    }
    return render(request, 'books.html', context)


def Student_books(request):
    
    book = Book.objects.filter(is_borrowed=True, borrowed_by_id=request.session['userid'])
    context = {'dataa': book}
    
    return render(request, 'borwoedbooks.html', context)


def borrowBook(req, bookID):

    book = Book.objects.filter(id=bookID)[0]
    context = {}
    if req.method == 'GET':
        context['flag'] = True
        form = BorrowBookForm(instance=book)
        context['form'] = form
        return render(req, 'borwoedbooks.html', context)
    elif req.method == 'POST':
        form = BorrowBookForm(instance=book, data=req.POST)
        if form.is_valid():
            form.save()
            Book.objects.filter(id=bookID).update(is_borrowed=True, borrowed_by_id_id=req.session['userid'])
            context['msg'] = "Successful Borrowing"
            context['color'] = "green"
            return HttpResponseRedirect('/Student_books')
        else:
            print(form.errors)
            context['msg'] = "Enter Valid Data"
            context['color'] = "red"
            context['form'] = BorrowBookForm(instance=book)
            return render(req, 'borwoedbooks.html', context)


def ReturnBook(req, bookID):

        book = Book.objects.filter(is_borrowed=True, borrowed_by_id=req.session['userid'])
        context = {'dataa': book}
        Book.objects.filter(id=bookID).update(is_borrowed=False, borrowed_by_id_id=None, returnTime=None)
        context['msg'] = "Successful Return"
        context['color'] = "green"
        return render(req, 'borwoedbooks.html', context)

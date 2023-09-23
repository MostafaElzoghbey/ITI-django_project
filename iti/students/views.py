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


def borrowBook(req, bookID):
    context = {}
    if req.session['username']:
        book = Book.objects.filter(id=bookID)[0]
        context = {}
        if req.method == 'GET':
            form = BorrowBookForm(instance=book)
            context['form'] = form
            return render(req, 'borwoedbooks.html', context)
        elif req.method == 'POST':

            form = BorrowBookForm(instance=book, data=req.POST)
            if form.is_valid():
                form.save()
                Book.objects.filter(id=bookID).update(
                    is_borrowed=True, borrowed_by_id_id=req.session['userid'])
                context['msg'] = "Borrowed Successfully"
                context['color'] = "green"
                return render(req, 'borwoedbooks.html', context)
            else:
                print(form.errors)
                context['msg'] = "Invalid Data"
                context['color'] = "red"
                context['form'] = BorrowBookForm(instance=book)
                return render(req, 'borwoedbooks.html', context)
        return HttpResponseNotAllowed()
    else:
        context['msg'] = "You Must Be Logged In to Borrow A Book."
        context['color'] = "red"
        context['form'] = BorrowBookForm()
        return render(req, 'borwoedbooks.html', context)


def Student_books(request):
    return render(request, 'borwoedbooks.html')

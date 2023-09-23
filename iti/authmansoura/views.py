from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .form import *
import sys
from .models import *
from students.models import *

# Create your views here.


def myRegister(request):
    if (request.method == 'POST'):
        Myaccount.objects.create(
            username=request.POST['Username'], password=request.POST['Password'], account=request.POST['Email'])
        return redirect('/Login')
    return render(request, 'Register.html')


def mylogin(request):
    context = {}
    if (request.method == 'POST'):
        usern = request.POST['Username']
        passw = request.POST['Password']
        try:
            obj = Myaccount.objects.filter(username=usern, password=passw)
            if (obj is not None):
                request.session['userid'] = obj[0].id
                request.session['username'] = obj[0].username
                request.session['account'] = obj[0].account
                if obj[0].is_admin == 'true':
                    request.session['is_admin'] = 1
                else:
                    request.session['is_admin'] = 0
                return HttpResponseRedirect('/')
            else:
                context['msg'] = 'invalide username or password'
        except:
            context['msg'] = sys.exc_info()[1]

    return render(request, 'Login.html', context)


def mylogout(request):
    request.session.clear()
    request.session.flush()
    return redirect('/Login')


def myprofile(request):
    context = {'profile': [Myaccount.objects.filter(
        id=request.session['userid'])[0]]}
    return render(request, 'profile.html', context)


def Update_profile(req, ID):
    train = Myaccount.objects.get(id=ID)
    form = updateprofile(instance=train)
    if (req.method == 'POST'):
        f = updateprofile(req.POST, instance=train)
        if (f.is_valid()):
            f.save()
            return HttpResponseRedirect('/profile')
    context = {'form': form}
    return render(req, 'updateProfile.html', context)


def AdminDashboard(req):

    bookss = Book.objects.all()
    users = Myaccount.objects.all()

    context = {
        'books': bookss,
        'users': users,
    }

    return render(req, 'admindashboard.html', context)


def Insert_Book(req):

    form = Newbookform()
    context = {}
    if (req.method == 'POST'):

        form = Newbookform(req.POST, req.FILES)

        if (form.is_valid()):

            form.save()
            return HttpResponseRedirect('/admindashboard')
        else:
            context['msg'] = 'enter valid data'

    context['form'] = form

    return render(req, 'insertbook.html', context)


def Update_Book(req, ID):

    book = Book.objects.get(id=ID)
    form = Newbookform(instance=book)
    if (req.method == 'POST'):

        f = Newbookform(req.POST, instance=book)

        if (f.is_valid()):

            f.save()
            return HttpResponseRedirect('/admindashboard')

    context = {'form': form}

    return render(req, 'updatebook.html', context)


def Delete_Book(req, ID):

    Book.objects.get(id=ID).delete()

    return HttpResponseRedirect('/admindashboard')


def search_student(request):

    bookss = Book.objects.all()
    users = Myaccount.objects.all()

    context = {
        'books': bookss,
        'users': users,
    }

    if request.method == 'POST':
        student_id = request.POST.get('student_id')

        student = Myaccount.objects.get(id=student_id)

        context = {
            'books': bookss,
            'users': [student],
        }
        return render(request, 'admindashboard.html', context)

    else:
        return render(request, 'admindashboard.html', context)

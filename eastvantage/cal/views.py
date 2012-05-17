# Create your views here.
from cal.models import Result
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class MathForm(forms.Form):
    expression = forms.CharField(max_length=100)


def home_view(request):
    if request.method.upper() == 'GET':
        if request.session.get('user_id'):
            return render(request, 'cal.html', {'result': None})
        else:
            return redirect('/login/')
    elif request.method.upper() == 'POST':
        if request.session.get('user_id'):
            form = MathForm(request.POST)
            if form.is_valid():
                result = None
                try:
                    result = eval(form.cleaned_data['expression'])
                except Exception, e:
                    result = e
                user = User.objects.get(id=request.session.get('user_id'))
                result = Result(user=user, expression=form.cleaned_data['expression'],
                                result=result)
                result.save()
            return render(request, 'cal.html', {'result': result.result})
        else:
            return redirect('/login/')


def login_view(request):
    if request.method.upper() == 'GET':
        if not request.session.get('user_id'):
            return render(request, 'login.html')
        else:
            return redirect('/')
    elif request.method.upper() == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request, user)
                request.session['user_id'] = user.id
                return redirect('/')
        return render(request, 'login.html', {'success': 'failed'})


def logout_view(request):
    logout(request)
    return redirect('/')

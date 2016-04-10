from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib import auth
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    login_form = AuthenticationForm()
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = auth.authenticate(username=_username,password=_password)
        if user is not None and user.is_active:
            auth.login(request,user)
            return HttpResponseRedirect('/')
        else:
            context = {'auth': False, 'form': login_form}
            return render(request,'users/login.html', context)
    else:
        return render(request,'users/login.html', {'form': login_form})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'base/dashboard.html')


def userLogin(request):
    if request.POST:
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
                messages.success(request, "Login Success")
            return redirect('dashboard')
        else:
            messages.error(request, "Username or password invalid")
    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    return redirect('dashboard')


def webUser(require):
    return render(request, 'web_management\eb_user.html')
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from .forms import CreateUserForm

def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm()
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'users/register.html', context=context)

def loginPage(request):
    return render(request, template_name='users/login.html')
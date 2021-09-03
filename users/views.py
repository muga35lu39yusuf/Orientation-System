from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def register():
    form = RegisterForm()
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('registration/login.html')
    else:
        #form = RegisterForm()
        form = RegisterForm()
    return render(response, 'registration/register.html',{'form':form})

def loggedout(request):

   return render(request, 'registration/loggedout.html')

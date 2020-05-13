from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import forms


# Create your views here.


def home(request):
    # dict={'name':"This is my view file"}
    return render(request, 'index.html')


def form_view(request):
    if request.method=='POST':
        form=forms.Loginform(request.POST)
        if form.is_valid():
            print("Validation worked")
            print("name :" + form.cleaned_data['name'])
            print("email :" + form.cleaned_data['email'])
            print("text :" + form.cleaned_data['text']) 
        # return redirect('home')


    form=forms.Loginform
    return render(request, 'register.html', {'form': form })

def home(request):
    return render(request,'home.html')

from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, UserPostForm
from django.contrib import messages

# Create your views here.
def user_login(request):
    form = AuthenticationForm(request=request,data= request.POST)
    messages.info(request, form.errors)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('post')

    form = AuthenticationForm()
    return render(request,'login.html', {'form': form})

def user_register(request):
    if request.method== 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Succesfully')
            return redirect('login')

    form= SignupForm()
    return render(request,'register.html',{'form':form})



@login_required(login_url='login')
def user_post(request):
    if request.method=='POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post')

    form= UserPostForm()
    return render(request,'post.html',{'form':form})
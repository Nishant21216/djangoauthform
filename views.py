from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django .http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
def Sign_up(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Accounted success!!!')
            fm.save()
    else:
        fm =UserCreationForm()
    return render(request,'enroll/signup.html',{'form':fm})

def User_login(request):
  
    if request.method=="POST":
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'LOgedd success!!!')
                return HttpResponseRedirect('/profile/')
    else:
        fm=AuthenticationForm()
    return render(request,'enroll/userlogin.html',{'form':fm})

def User_profile(request):
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')


def User_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def User_change(request):
 if request.user.is_authenticated:
    if request.method=="POST":
        fm = PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request,'password success!!!')
            return HttpResponseRedirect('/profile/')
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request,'enroll/changepass.html',{'form':fm})

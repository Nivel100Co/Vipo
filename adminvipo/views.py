from django.shortcuts import render
from django.views.generic import View
from .forms import *
from user.models import *
from django.shortcuts import render, redirect, get_object_or_404, render_to_response



class index(View):
    
    def get(self, request):
        # return render (request, 'session/base.html')
        return render (request, 'application/base.html')



class register(View):
    
    
    def post(self, request):
        if Register(request.POST).is_valid():
            user, create = Users.objects.get_or_create(username=Register(request.POST).data['email'])
            if create:
                user.email = Register(request.POST).data['email']
                user.first_name = Register(request.POST).data['fullname']
                saveuser.set_password(Register(request.POST).data['password'])
                return redirect('login')
            else:
                return render (request, 'session/register.html',{'form':Register(), 'user_exists':True})
        else:
            return render (request, 'session/register.html',{'form':Register(), 'not_valid_form':True})


    def get(self, request):
        return render (request, 'session/register.html', {'form':Register()})


class login(View):
    
    def get(self, request):
        return render (request, 'session/login.html', {'form':Login()})






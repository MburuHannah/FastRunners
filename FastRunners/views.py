from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
from FastRunners.models import Car
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate, logout

from django.http import JsonResponse
#Views connect your templates and models



# Create your views here.
def home(request):
    template = loader.get_template('Home.html')
    return HttpResponse(template.render({}, request))


def car_list(request):
    cars=Car.objects.all()
    template = loader.get_template('Cars_listing.html')
    context = {'cars': cars,}
    return HttpResponse(template.render(context, request))



def car_detail(request,car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars_detail.html', {'car':car})


def about_us(request):
    return render(request, 'About_us.html')


def contact_us(request):
    return render(request, 'Contact_Us.html')



def register(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user = form.save()
             user.set_password(form.cleaned_data.get('password1'))
             user.save()
             login(request, user)
             return redirect('home')  # Redirect to home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'User _Registration.html',{'form':form})



class CustomLoginView(LoginView):
      template_name ='User_Login.html'

def logout(request):
    return render(request,'Logout.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') # Redirect to a success page.
        else:
        # Return an 'invalid login' error message.
            return render(request, 'User_login.html', {'error': 'Invalid username or password'})
    else:
            return render(request, 'User_login.html')
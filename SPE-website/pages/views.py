from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

from .forms import MessagesForUsForm
import mimetypes
import os

def landing_page(request):
    return render(request, 'pages/landing-page.html')


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def gazette(request):
    return render(request, 'pages/gazette.html')


def gallery(request):    
    return render(request, 'pages/finalgallery.html')

def tgal(request):    
    return render(request, 'pages/testgal.html')

def tgal2(request):    
    return render(request, 'pages/tgal2.html')

def intern(request): 
    return render(request, 'pages/intern.html')

def teacher(request): 
    return render(request, 'pages/teacher.html')

def fipi(request): 
    return render(request, 'pages/fipi.html')

def basant(request): 
    return render(request, 'pages/basant.html')    

def cdd(request): 
    return render(request, 'pages/cdd.html')

def hall(request): 
    return render(request, 'pages/hall.html') 

def m(request): 
    return render(request, 'pages/m.html') 

def core_team(request):
    return render(request, 'pages/core-team.html')


def contact_us(request):
    if request.method == 'POST':
        form = MessagesForUsForm(request.POST)
        if form.is_valid():
            messageforus = form.save()
            subject = "message from django site"
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            sender_email= form.cleaned_data['sender_email']
            body = message + "\nEmail: " + sender_email + "\nName: "+ sender
            email=os.environ.get('USER_EMAIL') #add comany email
            try:
                send_mail(subject, body, email, [email])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            messages.success(request, f'Message sent!')
            return redirect('contact-page')
    else:
        form = MessagesForUsForm()
    context = {'form': form}
    return render(request, 'pages/contact-us.html', context)

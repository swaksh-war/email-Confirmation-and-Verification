from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')

def login_attempt(request):
    return render(request,'login.html')

def register_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            if User.objects.filter(username=username):
                messages.warning(request, 'Username is taken')
                return redirect('/register')
            if User.objects.filter(email=email):
                messages.warning(request, 'Email is already taken')
                return redirect('/register')
            user_obj = User.objects.create(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            email_send_verify(email, auth_token)
            
            return redirect('/token')
        
        
        except Exception as e:
            print(e)
            
        
        
    return render(request, 'register.html')

def success(request):
    return render(request, 'success.html')

def token(request):
    return render(request, 'token.html')

def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        
        if profile_obj.is_verified:
            messages.success(request,'your acccount is already verified')
            return redirect('/login')
        
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request,'Your Account is now Verified.')
            return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)

def error_page(request):
    return render(request,'error.html')
    

def email_send_verify(email, token):
    subject = 'Verify Your Account'
    message = "click on the link to get vefiried http://127.0.0.1:8000/verify/{}".format(token)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    
    


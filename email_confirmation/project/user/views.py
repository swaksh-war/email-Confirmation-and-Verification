from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from verify_email.email_handler import send_verification_email


def index(request):
    return render(request, 'user/index.html', {'title':'index'})

def register(request):
    form = UserRegisterForm(request.POST)
    if request.method== 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            
            htmly = get_template('user/Email.html')
            d = {'username':username}
            subject, from_email,to = 'NoReply', 'ghoshswakshwar@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, f'account created!')
            return redirect('login')
        else:
            form = UserRegisterForm()
    return render(request, 'user/register.html', {'form':form, 'title':'register here'})
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f'welcome {username}!!')
            return redirect('index')
        else:
            messages.success(request, f'no id found!')
    form= AuthenticationForm
    context = {
        'form':form,
        'title':'login'}
    return render(request, 'user/login.html', context)
                        
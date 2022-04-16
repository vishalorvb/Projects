from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    return render(request,'index.html')


def send_email(request):
    if request.method == 'POST':
        s = request.POST['email']
        print(s)
        subject = 'welcome to GFG world'
        message ="This is mail from Django app"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [s,]
        send_mail(subject, message, email_from, [s])

        return HttpResponse("Email sent")
    
   

    
from django.views import View
from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


class Homepage(View):
    def get(self, request):
        return render(request,'index.html')
    
    def post(self, request):
            
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        select_service = request.POST.get('select_service')
        select_price = request.POST.get('select_price')
        

        contact = Contact.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone,
                                        select_service=select_service, select_price=select_price)

        mail_subject = 'New Contact Form Submission'
        mail_message = f'First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nPhone: {phone}\n' \
                    f'Select Service: {select_service}\nSelect Price: {select_price}'

        send_mail(mail_subject, mail_message, settings.EMAIL_HOST_USER, [settings.COMPANY_EMAIL], fail_silently=False)

        messages.success(request, 'Your Request has been submitted. We will contact you soon. Thank you.')
        return render(request, 'index.html')
        
    
class About(View):
    def get(self, request):
        return render(request,'about.html')
    
class Service(View):
    def get(self, request):
        return render(request,'service.html')
    
class Properties(View):
    def get(self, request):
        return render(request,'properties.html')
    
class Gallery(View):
    def get(self, request):
        return render(request,'gallery.html')
    
class Contacts(View):
    def get(self, request):
        return render(request,'contact.html')
    

    def post(self, request):
            
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        select_service = request.POST['select_service']
        select_price = request.POST['select_price']
        comments = request.POST['comments']

        contact = Contact.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone,
                                        select_service=select_service, select_price=select_price, comments=comments)

        mail_subject = 'New Contact Form Submission'
        mail_message = f'First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nPhone: {phone}\n' \
                    f'Select Service: {select_service}\nSelect Price: {select_price}\nComments: {comments}'

        send_mail(mail_subject, mail_message, settings.EMAIL_HOST_USER, [settings.COMPANY_EMAIL], fail_silently=False)

        messages.success(request, 'Your Request has been submitted. We will contact you soon. Thank you.')
        return render(request, 'contact.html')
        
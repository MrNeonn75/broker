from django.shortcuts import render
from contact.models import ContactModel
from contact.forms import ContactForm
from blog.models import BlogModel
from .models import CampaignModel

def send_mail(request):
    form = ContactForm()

    if(request.method == 'POST'):
        
        if(form.is_valid):
            user_email= request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            name = request.POST['name']

            new_message = ContactModel.objects.create(
                name=name,
                user_email=user_email,
                subject=subject,
                message=message
            )


        else: 
            messages.error(request, 'Fill the form correctly!')

    return form


def index(request):
    property = CampaignModel.objects.all()
    last_blog = BlogModel.objects.order_by('-id')[:2]


    data = {
        'form' : send_mail(request),
        'property' : property,
        'blog' : last_blog,
    }

    return render(request, 'index.html', data)

def faqs(request):
    return render(request, 'faqs.html')

def about(request):
    return render(request, 'about.html')
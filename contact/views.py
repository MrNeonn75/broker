from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactModel
from .forms import ContactForm

def contact(request):
    form = ContactForm()
    if(request.method == 'POST'):
        
        # is_valid() -> False
        if(True):
            user_email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            name = request.POST['name']

            new_message = ContactModel.objects.create(
                user_email=user_email,
                subject=subject,
                message=message,
                name=name
            )

            return redirect('index')
        else: 
            messages.error(request, 'Error:)')


    data = {
        'form' : form,
    }

    return render(request, 'contact.html', data)

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm  # Ensure the form import is correct
from django.core.mail import send_mail
from django.conf import settings

def home_screen_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Compose the email message
            subject = f"New Contact Form Submission from {name}"
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            recipient_list = [settings.DEFAULT_FROM_EMAIL,'bhtyalphonce412@gmail.com','terilea.chesser@icloud.com']  # Set your recipient email in settings

            # Send email
            send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, recipient_list)
            
            # Display success message and redirect
            messages.success(request, "Your message has been sent!")
            return redirect('success')  # Redirect to a success page or message

        else:
            messages.error(request, "There was an error in your form. Please try again.")
    else:
        form = ContactForm()  # Display an empty form if the request is not POST

    return render(request, 'smilehub/home.html', {'form': form})

def success_view(request):
    return render(request, 'smilehub/success.html')

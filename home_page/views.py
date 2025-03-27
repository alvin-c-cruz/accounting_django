from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return render(request, 'home_page/index.html')

def about(request):
    return render(request, 'home_page/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email (Optional - if configured in settings.py)
        try:
            send_mail(
                f'Message from {name}',
                message,
                'alvin_c_cruz@yahoo.com',  # Sender email
                ['alvin_c_cruz@yahoo.com'],  # Your email where you want to receive messages
                fail_silently=False,
            )
            # Flash success message
            messages.success(request, "Thank you for your message. I’ll get back to you soon!")
        except Exception as e:
            # Flash error message if sending email fails
            messages.error(request, "Oops! Something went wrong. Please try again later.")

        # Redirect to the home page after submission
        return redirect('index')

    return render(request, 'home_page/contact.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings




@login_required
def homepage(request):
    return render(request,'sendmoney/homepage.html')



def send_money(request):
    return render(request, 'sendmoney/send_money.html')







@login_required
def about_us(request):
    return render(request, 'sendmoney/about_us.html')





@login_required
def track_transfer(request):
    return render(request, 'sendmoney/track_transfer.html')





@login_required
def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = cleaned_data['email']
            contact_number = cleaned_data['contact_number']
            message = cleaned_data['message']

            subject = 'New message from Contact Form'
            message_body = f'''
                 You have received a new message from the contact form:

                Name: {first_name} {last_name}
                Email: {email}
                Contact Number: {contact_number}
                Message: {message}  
            '''
            sender_email = email
            recipient_list = [settings.EMAIL_HOST_USER]
            try:
                # Send email to admin
                send_mail(subject, message_body, sender_email, recipient_list)

                # Send automated response to user
                user_subject = "Thank you for contacting us"
                user_message_body = f'''
                    Hi {first_name},

                    Thank you for reaching out to us. We have received your message and will get back to you soon.

                    Best regards,
                    Hamepage Team
                '''
                send_mail(user_subject, user_message_body, settings.EMAIL_HOST_USER, [email])

                success = True
                form = ContactForm()  # Clear the form after successful submission
            except Exception as e:
                print(f"Error sending email: {e}")
    else:
        form = ContactForm()
    return render(request, 'sendmoney/contact.html', {'form': form, 'success': success})
   



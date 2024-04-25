from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Testimonial
from .forms import TestimonialForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden


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
def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'sendmoney/testimonial_list.html', {'testimonials': testimonials})




def testimonial_create(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonial_list')
    else:
        form = TestimonialForm()
    return render(request, 'sendmoney/testimonial_form.html', {'form': form})





@login_required
def testimonial_update(request, pk):
    testimonial = get_object_or_404(Testimonial,pk=pk)
    if not request.user.is_superuser and testimonial.author != request.user:
        # Return a response indicating permission denied
        return HttpResponseForbidden("You do not have permission to update this testimonial.")

    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('testimonial_list')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'sendmoney/testimonial_form.html', {'form': form})




@login_required
def testimonial_delete(request, pk):
    testimonial = get_object_or_404(Testimonial,pk=pk)
    if not request.user.is_superuser and testimonial.author != request.user:
        return HttpResponseForbidden("You do not have permission to delete this testimonial.")
    
    testimonial.delete()
    return redirect('testimonial_list')









@login_required
def contact(request):
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
            send_mail(subject, message_body, sender_email, recipient_list)

            
            return render(request, 'sendmoney/contact_success.html')  
    else:
        form = ContactForm()
    return render(request, 'sendmoney/contact.html', {'form': form})
   



from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import NewsUserForm
from . models import NewsUsers


def newsletter_subscribe(request):

    if request.method == 'POST':
        form = NewsUserForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            if NewsUsers.objects.filter(email=instance.email).exists():
                messages.error(request, "Your Email Already exists in our database")
            else:
                instance.save()
                messages.success(request, 'Successfully added Email!')
                subject = 'Welcome to Tech Cloud!'
                html_message = render_to_string('email/mail_templates.html', {'context': 'values'})
                plain_message = strip_tags(html_message)
                from_email = 'Tech Cloud'
                send_mail(subject, plain_message, from_email, [instance.email], html_message=html_message)
                return redirect(reverse('home'))
    else:
        form = NewsUserForm()

    context = {'form': form}

    template = "newsletter/subscribe.html"
    return render(request, template, context)


def newsletter_unsubscribe(request):

    if request.method == 'POST':
        form = NewsUserForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            if NewsUsers.objects.filter(email=instance.email).exists():
                NewsUsers.objects.filter(email=instance.email).delete()
                messages.success(request, 'Successfully unsubscribe from Tech Cloud Newsletter!')
            else:
                messages.error(request, "Sorry but we did not find your email address in our database")
                return redirect(reverse('newsletter:unsubscribe'))
    else:
        form = NewsUserForm()

    context = {'form': form}

    template = "newsletter/unsubscribe.html"
    return render(request, template, context)

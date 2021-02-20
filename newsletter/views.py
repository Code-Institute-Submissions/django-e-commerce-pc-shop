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
                messages.success(request, 'Thank You for subscribe to Tech Cloud newletter!')
                subject = 'Welcome to Tech Cloud!'
                html_message = render_to_string('email/mail_subscribe.html', {'context': 'values'})
                plain_message = strip_tags(html_message)
                from_email = 'Tech Cloud'
                send_mail(subject, plain_message, from_email, [instance.email], html_message=html_message)
                return redirect(reverse('home'))
    else:
        form = NewsUserForm()

    context = {'form': form}

    template = "newsletter/subscribe.html"
    return render(request, template, context)



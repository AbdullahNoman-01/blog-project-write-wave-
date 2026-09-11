from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ContactMessageForm


def contact_view(request):

    if request.method == 'POST':
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Your message has been sent successfully! 🎉'
            )

            return redirect('contact')

    else:
        form = ContactMessageForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)
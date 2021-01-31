from django.shortcuts import render, redirect

from vichyawat.forms import ContactForm
from vichyawat.models import Contact


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Contact.objects.create(
                email=data['email'],
                subject=data['subject'],
                message=data['message']
            )
        return redirect('index')

    return render(request, "vichyawat/index.html")
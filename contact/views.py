from django.shortcuts import render, redirect
from contact.forms import ContactForm

def contact_new(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_sent')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

def contact_sent(request):
    return render(request, 'contact/contact_sent.html')

def mentorsandsupporters(request):
    if request.method == "POST":
        formmentor = ContactForm(request.POST)
        if formmentor.is_valid():
            formmentor.save()
            return redirect('contact_sent')
    else:
        formmentor = ContactForm()

    return render(request, 'contact/mentorsandsupporters.html', {'formmentor': formmentor})







# Create your views here.'''

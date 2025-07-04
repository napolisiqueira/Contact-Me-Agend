from django.shortcuts import render
from contacts.forms import ContactForm

def create(request):
    if request.method == "POST":
        context = {
            'form': ContactForm(request.POST)
        }

        return render(
            request,
            'contacts/create.html',
            context
        )
    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contacts/create.html',
        context
    )
from django.shortcuts import render, get_object_or_404
from contacts.models import Contact
from django.http import Http404


# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]
    context = {
        "contacts": contacts,
    }

    return render(
        request,
        'contacts\index.html',
        context
    )

def contact(request, id):
    single_contact = get_object_or_404(
        Contact.objects.filter(show=True),
        pk=id)
    context = {
        "contacts": single_contact,
    }

    return render(
        request,
        'contacts\contact.html',
        context
    )
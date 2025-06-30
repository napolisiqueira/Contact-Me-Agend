from django.shortcuts import render
from contacts.models import Contact


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
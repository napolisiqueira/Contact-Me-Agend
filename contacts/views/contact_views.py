from django.shortcuts import render, get_object_or_404, redirect
from contacts.models import Contact
from django.http import Http404


# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]
    context = {
        "contacts": contacts,
        "site_title": "Contatos"
    }

    return render(
        request,
        'contacts\index.html',
        context
    )

def contact(request, id):
    single_contact = get_object_or_404(Contact,pk=id, show=True)
    
    site_title = f"{single_contact.first_name} {single_contact.last_name} - "
    
    context = {
        "contacts": single_contact,
        "site_title": site_title
    }

    return render(
        request,
        'contacts\contact.html',
        context
    )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == "":
        return redirect("contacts:index")

    contacts = Contact.objects.filter(show=True).filter(first_name__icontains=search_value).order_by('-id')[:10]
    context = {
        "contacts": contacts,
        "site_title": "Search - "
    }

    return render(
        request,
        'contacts\index.html',
        context
    )

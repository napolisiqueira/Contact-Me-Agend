from django.shortcuts import render, redirect, get_object_or_404
from contacts.forms import ContactForm
from django.urls import reverse
from contacts.models import Contact
from django.contrib.auth.decorators import login_required

@login_required(login_url=('contacts:login'))
def create(request):
    form_action = reverse("contacts:create")

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        context = {
            "form": form,
            "form_action": form_action,
        }
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect("contacts:update", contact_id=contact.pk)

        return render(request, "contacts/create.html", context)

    context = {
        "form": ContactForm(),
        "form_action": form_action,
    }

    return render(request, "contacts/create.html", context)

@login_required(login_url=('contacts:login'))
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner= request.user)
    form_action = reverse("contacts:update", args=(contact_id,))

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
            "form": form,
            "form_action": form_action,
        }
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect("contacts:update", contact_id=contact.pk)

        return render(request, "contacts/create.html", context)

    context = {
        "form": ContactForm(instance=contact),
        "form_action": form_action,
    }

    return render(request, "contacts/create.html", context)

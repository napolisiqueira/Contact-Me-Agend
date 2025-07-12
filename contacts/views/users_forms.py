from django.shortcuts import render, redirect
from contacts.forms import RegisterForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from contacts.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.decorators import login_required



def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Usúario registrado!")
            return redirect("contacts:login")

    return render(request, "contacts/register.html", {"form": form})

@login_required(login_url='contacts:login')
def login_view(request):
    form = AuthenticationForm(request)

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, "Logado com sucesso!")
            return redirect("contacts:index")
        messages.error(request, "Login inválido!")

    return render(request, "contacts/register.html", {"form": form})

@login_required(login_url=('contacts:login'))
def logout_view(request):
    auth.logout(request)
    return redirect("contacts:login")


def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
    if request.method != "POST":
        return render(request, "contacts/user_update.html", {"form": form})
    form = RegisterUpdateForm(data=request.POST, instance=request.user)
    if not form.is_valid():
        return render(request, "contacts/user_update.html", {"form": form})
    form.save()
    return redirect("contacts:user_update")

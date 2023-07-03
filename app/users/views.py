from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import UserRegistrationForm


# Create your views here.
class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def get(self, request):
        context = {
            "form": UserRegistrationForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

        context = {
            "form": form,
        }
        return render(request, self.template_name, context)

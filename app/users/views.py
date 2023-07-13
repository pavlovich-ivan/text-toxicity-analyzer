from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserRegistrationForm, UserUpdateForm


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


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "registration/profile.html"


class EditPersonalDataView(LoginRequiredMixin, TemplateView):
    template_name = "registration/edit_personal_data.html"

    def get(self, request):
        context = {
            "form": UserUpdateForm(instance=request.user),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)

            return redirect("edit_personal_data")

        context = {
            "form": form,
        }
        return render(request, self.template_name, context)


class ChangePasswordView(LoginRequiredMixin, TemplateView):
    template_name = "registration/change_password.html"

    def get(self, request):
        context = {
            "form": PasswordChangeForm(request.user),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)

            return redirect("classifier")

        context = {
            "form": form,
        }
        return render(request, self.template_name, context)

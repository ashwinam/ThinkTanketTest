from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView

from .forms import SignInForm, SignUpForm
from .models import HobbiesTbl, UserTbl


class CustomLoginView(LoginView):
    template_name = 'signin.html'
    form_class = SignInForm
    redirect_authenticated_user = True

    


class CustomLogoutView(LogoutView):

    pass


class UserListView(LoginRequiredMixin, ListView):
    model = UserTbl
    template_name = 'user_list.html'
    context_object_name = 'users'
    paginate_by = 10
    ordering = ['-created_at']


class UserCreateView(LoginRequiredMixin, CreateView):
    model = UserTbl
    template_name = 'signup.html'
    form_class = SignUpForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs['hobbies'] = HobbiesTbl.objects.all()
        return super().get_context_data(**kwargs)
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        hobbies = request.POST.getlist('hobbies', None)
        print(hobbies, 'hhhh')
        form = SignUpForm(request.POST)


        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            print(form, '\n\n')

            if hobbies:
                form.hobbies.add(*hobbies)
            return redirect('user-list')
        else:
            print(form.errors)

        return render(request, 'signup.html')


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = UserTbl
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user-list')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = UserTbl
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('user-list')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs['hobbies'] = HobbiesTbl.objects.all()
        return super().get_context_data(**kwargs)
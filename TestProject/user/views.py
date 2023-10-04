from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.contrib.auth import login, authenticate

from .forms import SignInForm, SignUpForm
from .models import AgeTbl, HobbiesTbl, UserTbl
from datetime import datetime


def calculate_age(birthdate):
    
    # birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    
    
    current_date = datetime.now()
    
    
    age = current_date.year - birthdate.year
    

    if current_date.month < birthdate.month or (current_date.month == birthdate.month and current_date.day < birthdate.day):
        age -= 1
    
    print(age)

    return age

def login_view(request):
    if request.user.is_authenticated:
        return redirect('user-list')
    if request.method == 'POST':
        print(request.POST)
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('user-list')  # Redirect to a success page, e.g., 'home'
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})

    


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
        form = SignUpForm(request.POST)


        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            
            age = calculate_age(form.date_of_birth)
            
            if age:
                age_obj = AgeTbl.objects.create(age=age)
                form.age = age_obj

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
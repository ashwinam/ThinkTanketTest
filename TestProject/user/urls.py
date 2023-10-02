from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('create/', views.UserCreateView.as_view(), name="create-user"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('user/delete/<int:pk>/', views.UserDeleteView.as_view(), name='user-delete'),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view(), name='user-update'),
]

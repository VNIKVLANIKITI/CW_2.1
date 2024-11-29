from users.forms import UserRegisterForm, UserEditForm
from django.views.generic import CreateView, UpdateView
from users.models import User
from django.urls import reverse_lazy


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy('users:login')


class EditView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = "users/edit.html"
    success_url = reverse_lazy('users:edit')

    def get_object(self, queryset=None):
        return self.request.user

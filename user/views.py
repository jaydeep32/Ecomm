from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from user.forms import LoginForm

# Create your views here.


class CustomeLogin(LoginView):
    template_name = 'user/login.html'
    authentication_form = LoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('product:home')
        return super().dispatch(request, *args, **kwargs)
    


from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView


app_name = 'user'

urlpatterns = [
    path('login/', views.CustomeLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]



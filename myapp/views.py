from audioop import reverse
from re import I
# from msilib.schema import ListView
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404

from django.urls import reverse_lazy
from myapp.models import CustomUser, Message
from .forms import SignUpForm, LoginForm, MessageForm
from django.views.generic import TemplateView, ListView,UpdateView
from django.views.generic.edit import CreateView 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "myapp/index.html")

class Signup(CreateView):
    form_class = SignUpForm
    model = CustomUser
    template_name = 'myapp/signup.html'
    success_url = reverse_lazy('index')

class Login(LoginView):
    form_class = LoginForm
    tamplate_name = 'myapp/login.html'

class Friends(LoginRequiredMixin, ListView):
    template_name = 'myapp/friends.html'
    model = CustomUser
    context_object_name = 'user_list'

    def get_success_url(self):
        return reverse(kwargs={'pk': self.object.id})

class Logout(LogoutView):
    template_name = 'myapp/logout.html'

class Talkroom(LoginRequiredMixin, UpdateView,):
    model = CustomUser


def friends(request):
    return render(request, "myapp/friends.html")

@login_required
def talk_room(request, pk):
    messages = Message.objects.all()
    users = CustomUser.objects.all()
    if request.method == "POST":
       form = MessageForm(request.POST)
       if form.is_valid():
           form.save()
    else:
        form = MessageForm()

    context = {
        "messages": messages,
        "pk": pk,
        "form":form,
        "users":users
        }
    return render(request, "myapp/talk_room.html", context)

def setting(request):
    return render(request, "myapp/setting.html")

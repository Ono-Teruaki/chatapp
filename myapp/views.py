from audioop import reverse
from re import I
from django.shortcuts import redirect, render, get_object_or_404, resolve_url
from django.http import Http404
from django.contrib import messages
from django.db.models import Q 
from django.urls import reverse_lazy
from myapp.models import CustomUser, Message
from .forms import SignUpForm, LoginForm, MessageForm
from django.views.generic import TemplateView, ListView,UpdateView
from django.views.generic.edit import CreateView 
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#初期画面
def index(request):
    return render(request, "myapp/index.html")

#会員登録画面
class Signup(CreateView):
    form_class = SignUpForm
    model = CustomUser
    template_name = 'myapp/signup.html'
    success_url = reverse_lazy('index')

#ログイン画面
class Login(LoginView):
    form_class = LoginForm
    tamplate_name = 'myapp/login.html'

#友達表示
class Friends(LoginRequiredMixin, ListView):
    template_name = 'myapp/friends.html'
    model = CustomUser
    context_object_name = 'user_list'
    #友達検索部分
    def get_queryset(self): 
        queryset = CustomUser.objects.order_by('date_joined')
        query = self.request.GET.get('query')

        if query:
            queryset = queryset.filter(Q(username__icontains=query))
        return queryset

#トークルーム
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

#設定部分
def setting(request):
    return render(request, "myapp/setting.html")

#名前変更
class NameChangeView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "myapp/namechange.html"
    fields = ['username']
    success_url = reverse_lazy('name_change_done')

#名前変更確認
@login_required
def name_change_done(request):
    return render(request, "myapp/namechange_done.html")

#メールアドレス変更
class emailChangeView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "myapp/emailchange.html"
    fields = ['email']
    success_url = reverse_lazy('email_change_done')

#メアド変更確認
@login_required
def email_change_done(request):
    return render(request, "myapp/emailchange_done.html")

#アイコン画像変更
class ImageChangeView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "myapp/imagechange.html"
    fields = ['image']
    success_url = reverse_lazy('image_change_done')

#アイコン変更確認
@login_required
def image_change_done(request):
    return render(request, "myapp/imagechange_done.html")

#パスワード変更
class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    model = CustomUser
    success_url = reverse_lazy('password_change_done')
    template_name = 'myapp/passwordchange.html'
    
#パスワード変更確認
class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'myapp/passwordchange_done.html'

#ログアウト
class Logout(LogoutView):
    template_name = 'myapp/index.html'


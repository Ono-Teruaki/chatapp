from django.urls import path
from . import views
from intern import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.Signup.as_view(), name='signup_view'),
    path('login', views.Login.as_view(), name='login_view'),
    path('friends', views.Friends.as_view(), name='friends'),
    path('<pk>/talk_room/', views.talk_room, name='talk_room'),
    path('setting', views.setting, name='setting'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('<int:pk>/name_change/', views.NameChangeView.as_view(), name='name_change'),
    path('name_change_done', views.name_change_done, name='name_change_done'),
    path('<int:pk>/email_change/', views.emailChangeView.as_view(), name='email_change'),
    path('email_change_done', views.email_change_done, name='email_change_done'),
    path('<int:pk>/image_change/', views.ImageChangeView.as_view(), name='image_change'),
    path('imagechange_done', views.image_change_done, name='image_change_done'),
    path('password_change', views.PasswordChange.as_view(), name='password_change'),
    path('password_change_done', views.PasswordChangeDone.as_view(), name='password_change_done')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
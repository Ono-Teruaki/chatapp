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
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
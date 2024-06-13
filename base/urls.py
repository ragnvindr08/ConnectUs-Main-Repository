from django.urls import path, include
from .views import authView, home
from django.conf import settings
from django.conf.urls.static import static
from . import views 
from .views import messages_view
from .views import messages_home

urlpatterns = [
    path("home/", home, name="home"),
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),   
    path('registrations/signup.html', authView,name='signup'),
    path('community/', views.community, name='community'), 
    path('developer/', views.developer, name='developer'), 
    path('messages/', messages_view, name='messages'), #messages url connected siya sa view.py yung messages_view
    path('homemessages/', messages_home, name='messageshome'),
    path('create_post/', views.create_post, name='create_post'),
    path('user/<str:username>/', views.user_posts, name='user_posts'),
    path('timeline/', views.timeline, name='timeline'),
    path('timeline-home/', views.timelinehome, name='timelinehome'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
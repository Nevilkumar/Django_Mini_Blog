from django.urls import path, include
from blog import views as blog_views

urlpatterns = [
    path('', blog_views.home, name='home'),
    path('dashboard/', blog_views.dashboard, name='dashboard'),
    path('login/', blog_views.user_login, name='user_login'),
    path('signup/', blog_views.user_signup, name='user_signup'),
    path('logout/', blog_views.user_logout, name='user_logout'),
    path('addpost/', blog_views.add_post, name='addpost'),
    path('updatepost/<int:id>/', blog_views.update_post, name='updatepost'),
    path('deletepost/<int:id>/', blog_views.delete_post, name='deletepost'),

]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

    path('feed/', views.feed_view, name='posts_feed'),
    path('post/create/', views.create_post_view, name='create_post'),

    path('profiles/', views.profiles_view, name='profiles'),
    path('profile/<int:profile_id>/', views.profile_detail_view, name='profile_detail'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),

    path('jobs/', views.jobs_view, name='jobs'),
    path('events/', views.events_view, name='events'),
    path('mentorship/', views.mentorship_view, name='mentorship'),
    path('messages/', views.messages_view, name='messages'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

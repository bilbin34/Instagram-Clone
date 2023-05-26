from django.urls import path
from post import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registration/', views.registration, name="registration"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('editprofile/', views.editprofile, name="editprofile" ), 
    path('addpost/', views.addpost, name="addpost"),
    path('editpost/<int:id>', views.editpost, name="editpost"),
    path('delete/<int:id>', views.delete, name="delete"),  
    path('views/<int:id>', views.views, name="views"),
    path('search/', views.search, name="search"),
    path('profile2/<int:pid>', views.profile2, name="profile2"),
]




from django.urls import path
from . import views
urlpatterns = [

    path('',views.demo,name='demo'),
    path('home', views.home, name='home'),
    path('ho', views.ho, name='ho'),
    path('register',views.register,name='register'),
    path('logout', views.logout, name='logout'),
    path('login',views.login,name='login'),
    path('details', views.details, name='details'),
    path('det', views.det, name='det'),
    path('deta', views.deta, name='deta'),
    path('add/',views.add_movie,name='add_movie'),
    path('review',views.review,name='review'),
    # path('add',views.add_movi,name='add_movi'),
    path('detail/<int:movie_id>/', views.detail,name='detail'),
    path('de/<int:movie_id>/', views.de, name='de'),

    path('update/<int:id>/', views.update, name='update'),
    # path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('cut/<int:id>/', views.cut, name='cut'),

    path('film',views.film,name='film'),
    path('rev', views.rev, name='rev'),


]
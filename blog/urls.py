from django.urls import path
from . import views

urlpatterns = [

        path('',views.index, name ='index page'),
        path('home/',views.home, name ='Home page'),
        path('signup/',views.signup, name ='Register'),
        #path('login/',views.login, name ='Login'),
        path('quiz/',views.quiz, name ='Quiz'),

]

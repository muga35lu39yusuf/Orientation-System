from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [

        path('',views.index, name ='index page'),
        path('home/',views.home, name ='Home page'),
        path('signup/',views.signup, name ='Register'),
        #path('login/',views.login, name ='Login'),
        path('quiz/',views.quiz, name ='Quiz'),
        path('report/',views.report, name ='Report'),
        #path('pdf/',views.render_pdf_view, name ='PDFReport'),
        path('formView/',views.formView, name ='formView'),
        path('loggedout/',user_views.loggedout, name ='loggedout'),
        path('start/',views.start, name ='start'),


]

from django.urls import path
from medicaltrust import views

urlpatterns = [
    path('medical',views.medical,name="medical"),
    path('trust',views.trust,name="trust"),
    path('home',views.home,name="home"),
    path('service',views.service,name="service"),
    path('booking/<int:id>',views.booking,name="booking"),
    path('appoinment',views.appoinment,name="appoinment"),
    path('contact',views.contact,name='contact'),
    path('Register',views.Register,name="Register"),
    path('list/<int:id>',views.list,name="list"),
    path('login',views.login,name="login"),
    path('Ulogin',views.Ulogin,name="Ulogin"),
    path('userlogout',views.userlogout,name="userlogout"),
    path('acdata/<int:id>',views.acdata,name="acdata"),
    path('activity',views.activity,name="activity"),
    path('cancel/<int:id>',views.cancel,name="cancel")
    
]

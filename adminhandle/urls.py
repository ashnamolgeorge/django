from django.urls import path
from.import views


urlpatterns = [
    path('details',views.details,name="details"),
    path('form',views.form,name="form"),
    path('table',views.table,name="table"),
    path('usertable',views.usertable,name="usertable"),
    path('Ucontact',views.Ucontact,name="Ucontact"),
    path('add',views.add,name="add"),
    path('actable',views.actable,name="actable"),
    path('remove/<int:id>',views.remove,name="remove"),
    path('approve/<int:id>',views.approve,name="approve"),
    path('aptable',views.aptable,name="aptable")
]
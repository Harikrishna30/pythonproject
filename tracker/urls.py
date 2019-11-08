from django.contrib import admin
from django.urls import path

from .import views
urlpatterns = [
    path('index/',views.index,name='indexpage'),
    path('registation/',views.register,name='registerpage'),
    path('walkins/',views.walkins,name='walkinspage'),
    path('callings/',views.callings,name='callingspage'),
    path('counclling/',views.counclling,name='councllingpage'),
    path('joining/',views.Joining,name='joiningpage'),
    path('joinings/<id>',views.Joinings,name='joiningspage'),
    path('willing/<id>',views.Willing,name='willingpage'),
    path('dead/<id>', views.Dead, name='dead'),
    path('students/', views.Students, name='studentspage'),
    path('update/<id>', views.Rejoin, name='update'),
    path('currentstatus/', views.Currentstatus, name='currentstatus'),
    path('complete/<id>', views.Complete, name='complete'),
    path('stopped/<id>', views.Stopped, name='stopped'),

]

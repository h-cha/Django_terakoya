# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
        path('',views.home,name='home'),
        path('Ksetumei',views.Ksetumei,name='Ksetumei'),
        path('Kcreate',views.Kcreate,name='Kcreate'),
        path('Kresult',views.Kresult,name='Kresult'),
        path('Rsetumei',views.Rsetumei,name='Rsetumei'),
        path('Rquestion',views.Rquestion,name='Rquestion'),
        path('Rresult',views.Rresult,name='Rresult'),
        ]
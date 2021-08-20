from django.urls import path
from . import views

#creating urls from main url.py located in learning_project
urlpatterns = [
    path('home/', views.home,name='learning-home'),
    path('about/',views.about,name='learning-about'),
    path('add/',views.add,name='learning-dataadd'),
    path('delete/',views.delete,name='learning-datadelete'),
    path('viewdata/',views.viewdata,name='learning-view')
]


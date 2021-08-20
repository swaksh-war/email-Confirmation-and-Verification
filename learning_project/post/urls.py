from django.urls import path
from . import views

#urls that contains paths to go inside include('post.url') in the main urls file
urlpatterns=[
    path('newpost/',views.create,name='new-post'),
    path('',views.shit,name='shit-post'),
    path('view/',views.viewpost,name='view-post'),
    path('delete/',views.delete,name='delete-post'),
    path('update/',views.update,name='update-post'),
    path('update/successtext/',views.success,name='success-text')
    ]
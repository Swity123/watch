
from django.urls import path
from .views import *

urlpatterns = [
    path('',watch_list, name='main'),
    path('viewdetail/<int:pk>',view_watch, name='view_watch'),
    path('editwatch/<int:pk>',edit_watch,name='edit_watch'),
    path('delwatch/<int:pk>',delete_watch,name='delete_watch')
]

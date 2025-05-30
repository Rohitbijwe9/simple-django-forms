'''
from django.urls import path
from .views import UserFormView,show


urlpatterns=[
    path('userfor/',UserFormView,name='userform_url'),
    path('show/',show,name='show_url')
]


'''
from django.urls import path
from .views import UserFormView,show_user_view


urlpatterns=[
    path('userform/',UserFormView,name='user_url'),
    path('show/',show_user_view,name='show_url')
]




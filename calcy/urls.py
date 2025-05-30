from django.urls import path
from . views import CalcyView

urlpatterns=[
    path('calcy/',CalcyView)
]
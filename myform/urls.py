
from django.urls import path
from .views import FormView

urlpatterns = [

    path('', FormView, name='form'),

]


from django.urls import path
from .views import person_create

urlpatterns = [

    path('', person_create, name='person_create'),

]

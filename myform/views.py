from django.shortcuts import render 
# Create your views here.


def FormView(request):

    return render(request , 'form.html')
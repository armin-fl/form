from django.shortcuts import render, redirect
from .forms import PersonForm
from django.http import HttpResponse

def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success", content_type="text/plain")  # Redirect to a success page or another view
        else:
            print("Form is not valid")
            print(form.errors)  # This will print the form errors in the console
    else:
        form = PersonForm()
    return render(request, 'person_form.html', {'form': form})

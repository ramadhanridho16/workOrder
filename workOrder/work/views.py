from django.shortcuts import render
from .forms import NewItemForm

# Create your views here.
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or do something else upon successful form submission
    else:
        form = NewItemForm()
    return render(request, 'work.html', {'form': form})
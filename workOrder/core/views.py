from django.shortcuts import render, redirect
from work.models import Report
# from item.models import Category, Item
from .forms import SignupForm


def index(request):
    reports = Report.objects.all()
    return render(request, 'core/index.html', {'reports': reports})


# def contact(request):
#     return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

# def report_table(request):
#     reports = Report.objects.all()      # Retrieve all rows from reports table
#     return render(request, "")
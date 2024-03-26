from django.shortcuts import render, redirect
from .models import Report
# from item.models import Category, Item
from .forms import SignupForm

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from .forms import NewItemForm, EditItemForm
from .models import Report


# def index(request):
#     reports = Report.objects.all()
#     return render(request, 'core/index.html', {'reports': reports})

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



@login_required
def work_list(request):
    reports = Report.objects.all()
    return render(request, 'core/task_list.html', {'reports': reports})

@login_required
def work_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'core/task_detail.html', {'reports': report})

@login_required
def work_create(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:work_list')
    else:
        form = NewItemForm()
    return render(request, 'core/task_form.html', {'form': form})

@login_required
def work_update(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        form = EditItemForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('core:work_list')
    else:
        form = EditItemForm(instance=report)
    return render(request, 'core/task_form.html', {'form': form})


@login_required
def work_delete(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        report.delete()
        return redirect('core:work_list')
    return render(request, 'core/task_confirm_delete.html', {'report': report})
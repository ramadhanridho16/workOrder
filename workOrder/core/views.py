from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Report
from datetime import datetime, timedelta
# from item.models import Category, Item
from .forms import SignupForm

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from .forms import NewItemForm, EditItemForm, DateSearchForm
from .models import Report


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

    return render(request, 'core/task_list.html', {
        'reports': reports,
        })

@login_required
def work_search(request):
    global start_date, end_date
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        data = Report.objects.filter(jam__range=[start_date, end_date])
    else:
        data = Report.objects.all()

    # penambahan pencarian untuk status pending, selesai, dan tahap rencana

    return render(request, 'core/task_search.html', {
        'data': data,
        'start_date':start_date,
        'end_date':end_date
        })

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
    return render(request, 'core/task_confirm_delete.html', {'report':report})

@login_required
def cetak(request):
    data = None
    global start_date, end_date
    # Lakukan operasi cetak dengan menggunakan start_date dan end_date
    if data == None:
        data = Report.objects.all()
    if start_date and end_date:
        data = Report.objects.filter(jam__range=[start_date, end_date])

    return render(request, 'core/cetak.html', {
        'data': data,
        'start_date': start_date,
        'end_date': end_date
    })


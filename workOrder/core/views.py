from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Report, Status
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
    global start_date, end_date, status_id
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    # statuses = Status.objects.all()
    status_id = request.GET.get('status', None)
    data = Report.objects.all()

    if start_date and end_date:
        data = Report.objects.filter(tanggal__range=[start_date, end_date])
    # else:
    #     data = Report.objects.all()
    
    if status_id:
        data = data.filter(status__status__iexact=status_id)

    # status = Report.objects.filter(jam__range=[start_date, end_date])
    # if status:
    #     status = status.filter(Q(name__icontains=status))

    # penambahan pencarian untuk status pending, selesai, dan tahap rencana
    

    return render(request, 'core/task_search.html', {
        'data': data,
        'start_date':start_date,
        'end_date':end_date,
        'status_id':status_id,
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
    data = Report.objects.all()
    global start_date, end_date, status_id
    # penambahan start_date (untuk )
    # start_date = request.GET.get('start_date', None)
    # end_date = request.GET.get('end_date', None)
    # status_id = request.GET.get('status_id', None)
    # Lakukan operasi cetak dengan menggunakan start_date dan end_date
    if data == None:
        data = Report.objects.all()
    if start_date and end_date:
        data = Report.objects.filter(tanggal__range=[start_date, end_date])
    if status_id:
        data = data.filter(status__status__iexact=status_id)

    return render(request, 'core/cetak.html', {
        'data': data,
        'start_date': start_date,
        'end_date': end_date,
        'status_id':status_id
    })

import csv
import xlwt

def download_excel(request):
    # Retrieve filtering parameters
    global start_date, end_date, status_id
    # start_date = request.GET.get('start_date', None)
    # end_date = request.GET.get('end_date', None)
    # status_id = request.GET.get('status_id', None)

    # Apply filtering
    data = Report.objects.all()
    if start_date and end_date:
        data = data.filter(tanggal__range=[start_date, end_date])
    if status_id:
        data = data.filter(status__status__iexact=status_id)

    # Sort the data
    # data = data.order_by('tanggal')  # You can adjust the sorting criteria as per your requirement

    # Create Excel file
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Data')

    # Write headers
    headers = ['Jam', 'Tanggal', 'Jenis Pekerjaan', 'Unit', 'Pelaksana', 'Status', 'Keterangan']
    for col, header in enumerate(headers):
        ws.write(0, col, header)

    # ws.write(row_num + 1, 1, report.tanggal.strftime('%Y-%m-%d') if report.tanggal else '')
    # Write data rows
    for row_num, report in enumerate(data):
        ws.write(row_num + 1, 0, report.jam)
        ws.write(row_num + 1, 1, report.tanggal)
        ws.write(row_num + 1, 2, report.jenis_pekerjaan.pekerjaan)
        ws.write(row_num + 1, 3, report.user.pengguna)
        ws.write(row_num + 1, 4, report.pelaksana.pelaksana)
        ws.write(row_num + 1, 5, report.status.status)
        ws.write(row_num + 1, 6, report.keterangan)

    wb.save(response)
    return response



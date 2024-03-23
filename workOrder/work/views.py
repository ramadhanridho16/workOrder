from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from .forms import NewItemForm, EditItemForm
from .models import Report

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

@login_required
def index(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or do something else upon successful form submission
    else:
        form = NewItemForm()
    return render(request, 'work/form.html', {'form': form})

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST)

        if form.is_valid():
            report = form.save(commit=False)
            report.created_by = request.user
            report.save()

            return redirect('core:index', pk=report.id)

    else:
        form = NewItemForm()

    return render(request, 'work/form.html', {
        'form': form,
        'title': 'New Item',
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Report, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)

    else:
        form = EditItemForm(instance=item)

    return render(request, 'work/form.html', {
        'form': form,
        'title': 'New Item',
    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Report, pk=pk, )
    item.delete()
    return redirect('dashboard:index')
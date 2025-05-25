from django.shortcuts import render, redirect

from app.forms import IzlozhbaForm
from app.models import Izlozhba


# Create your views here.


def index(request):
    izlozhbi = Izlozhba.objects.all()
    context = {'izlozhbi': izlozhbi}
    return render(request, 'index.html', context=context)


def add(request):
    if request.method == 'POST':
        form = IzlozhbaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'add.html', context={'form': IzlozhbaForm()})

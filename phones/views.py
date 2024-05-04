from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import PhoneForm
from .models import Phones, Category


# Create your views here.


# Create your views here.
def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)


def get_phones(request, pk):
    phones = Phones.objects.filter(category=pk)
    context = {
        'phones': phones
    }
    return render(request, 'phones.html', context=context)


def detail(request, pk):
    phone = Phones.objects.get(pk=pk)
    context = {
        'phone': phone
    }
    return render(request, 'detail.html', context=context)


def add_phones(request):
    form = PhoneForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('phones:get_info')
    context = {
        'form': form
    }
    return render(request, 'create.html', context=context)


def update_phones(request, pk):
    data = Phones.objects.get(pk=pk)
    form = PhoneForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        print(1)
        form.save()
        return redirect('phones:get_info')
    context = {
        'form': form
    }
    return render(request, 'update.html', context=context)

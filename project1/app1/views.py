from django.shortcuts import render

from .train import Train

def index (request):
    return render(request , 'index.html')

def show_all_trains(request):
    context = {}
    context['trains'] = Train.objects.all()

    return render(request, 'trains.html', context)

def show_single_train(request, train_number):
    context = {}
    context['train'] = Train.objects.filter(train_number = train_number).first()

    return render(request, 'train-detail.html', context)    
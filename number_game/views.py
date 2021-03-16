from django.shortcuts import render, redirect
import random

def index(request):
    if 'number' not in request.session:
        num = random.randint(1, 100)
        request.session['number'] = num
        print(request.session['number'])
    else:
        print("Key exists.")
    return render(request, 'index.html')

def process(request):
    print(request.POST)
    request.session['guess_number'] = request.POST['guess']

    if int(request.session['guess_number']) == int(request.session['number']):
        return redirect('/correct')

    elif int(request.session['guess_number']) > int(request.session['number']):
        return redirect('/too_high')

    elif int(request.session['guess_number']) < int(request.session['number']):
        return redirect('/too_low')

def correct(request):
    del request.session['number']
    return render(request, 'correct.html')

def too_high(request):
    return render(request, 'too_high.html')

def too_low(request):
    return render(request, 'too_low.html')
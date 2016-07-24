# -*- coding:utf-8 -*-

from redis import Redis
from django.shortcuts import render, redirect

from .models import Item


redis = Redis(host='redis', port=6379)


def home(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    counter = redis.incr('counter')
    return render(request, 'home.html', {'items': items, 'counter': counter})

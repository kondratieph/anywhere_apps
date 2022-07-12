from django.shortcuts import render, HttpResponse

def start(request):
    return render(request, 'common/start.html')

def test(request):
    return render(request, 'common/test.html')


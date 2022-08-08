from django.shortcuts import render, HttpResponse

def start(request):
    # context = {
    #     'title': 'Demo Apps',
    #     # 'to_do_list': None,
    #     # 'news': None
    # }
    return render(request, 'common/start.html')

def test(request):
    return render(request, 'common/test.html')


from django.shortcuts import render


def indexview(request):
    return render(request=request, template_name='songs/index-dev.html')

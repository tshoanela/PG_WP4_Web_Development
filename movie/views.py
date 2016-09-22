from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):

    template = loader.get_template('movie/index.html')
    return HttpResponse(template.render(request))
    #return render(request,'movie/index.html',context=None)

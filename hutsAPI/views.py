from django.http import Http404
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from hutsAPI.models import Hut


def index(request):
        huts = Hut.objects.all()
        return render_to_response("index.html",RequestContext(request,
                                             {'huts': huts}))

def detail(request, hut_id):
    try:
        hut = Hut.objects.get(pk=hut_id)
    except Hut.DoesNotExist:
        raise Http404("HUT does not exist")
    return render(request, 'detail.html', {'hut': hut})

def map(request):
        huts = Hut.objects.all()
        return render_to_response("map.html",RequestContext(request,
                                             {'huts': huts}))
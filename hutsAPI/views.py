from django.http import Http404
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from hutsAPI.models import Building, Hut


def index(request):
        buildings = Building.objects.all().order_by('street','number')
        return render_to_response("index.html",RequestContext(request,
                                             {'huts': buildings}))

def detail(request, hut_id):
    try:
        building = Building.objects.get(pk=hut_id)
    except Hut.DoesNotExist:
        raise Http404("HUT does not exist")
    return render(request, 'detail.html', {'building': building})

def map(request):
        buildings = Building.objects.all()
        return render_to_response("map.html",RequestContext(request,
                                             {'huts': buildings}))
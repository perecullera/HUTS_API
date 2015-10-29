from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from hutsAPI.models import Hut


def index(request):
        huts = Hut.objects.all()
        return render_to_response("index.html",RequestContext(request,
                                             {'huts': huts}))
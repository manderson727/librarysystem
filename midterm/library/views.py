from django.shortcuts import render
from django.http import HttpResponse
from library.forms import MediaForm
from library.models import Media, MediaInstance
from django.db.models import Q
import datetime as date

def index(request):
    #return HttpResponse("Library Tracking System <a href='/library/about/'>About</a>")
    return render(request, "library/index.html", {})

def about(request):
    #return HttpResponse("About Page <a href='/library/'>Index</a>")
    return render(request, "library/about.html", {})

def checkedout(request):
    checkedout_list = MediaInstance.objects.order_by('due')
    for inst in checkedout_list:
        if inst.due < date.date.today(): # date.today():
            inst.fine = (date.date.today() - inst.due).days

    context_dict = {'checkedout': checkedout_list}

    return render(request, "library/checkedout.html", context_dict)

def search_form(request):
    return render(request, 'library/search_form.html')

def search(request):
    if 'q' in request.GET: # and request.GET['q']:
        q = request.GET['q']
        Medias = Media.objects.filter(Q(title__icontains=q) | Q(type__icontains=q) | Q(isbn__icontains=q))
        return render(request, 'library/search_results.html', {'Medias': Medias, 'query': q})
    else:
        return HttpResponse('Please submit a search title')

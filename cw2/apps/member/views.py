from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from django.template import loader
from .models import Member
def index(request):
    template = loader.get_template('myfirst.html')
    mymembers = Member.objects.all().values()
    context = {'mymember': mymembers}
    return HttpResponse(template.render(context, request))

def search(request):
    template = loader.get_template('search.html')
    namesearch = request.GET['search']
    mymembers = Member.objects.filter(name__icontains=namesearch)
    context = {'mymember': mymembers}
    return HttpResponse(template.render(context, request))
from django.shortcuts import render
from django.http import HttpResponse
from .models import  Published ,Featured,Generalpage,Propheticpage ,Spiritualpage ,Socialpage,Count ,Articles
# Create your views here.
def index(request):
   
    dict_pb={
     'pb':Published.objects.all()
    }
    dict_ct={
     'ct':Count.objects.all()
    }
    dict_ft={
        'ft':Featured.objects.all()
    }
    dict_art={
     'art':Articles.objects.all()
    }
  
    dict_re = {**dict_art,**dict_pb ,**dict_ft  ,**dict_ct }
    
    return render(request,'index.html', dict_re )

def featurepage(request):
    
    dict_ft={
        'ft':Featured.objects.all()
    }
  
    return render(request,'featured.html', dict_ft)

def articlepage(request):
    dict_art={
     'art':Articles.objects.all()
    }
   
    return render(request,'article.html', dict_art)

def generalpage(request): 
    dict_gn={
        'gn':Generalpage.objects.all()
    }

    return render(request,'general.html',dict_gn)

def propheticpage(request):
    dict_pr={
        'pr':Propheticpage.objects.all()
    }

    return render(request,'prophetic.html',dict_pr)

def spiritualpage(request):
    dict_sp={
        'sp':Spiritualpage.objects.all()
    }

    return render(request,'spiritual.html',dict_sp)

def socialpage(request):
    dict_sc={
        'sc':Socialpage.objects.all()
    }

    return render(request,'social.html',dict_sc)
def aboutpage(request):
 
    return render(request,'about.html')
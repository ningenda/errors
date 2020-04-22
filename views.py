from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def help (request):
    helpdict={'help_insert':"hello this is <em>ningen</em> coming from view.py"}
    return render(request,'apptwo/help.html',context=helpdict)

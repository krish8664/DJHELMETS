from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.

def home(request):
    print "hello"
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))
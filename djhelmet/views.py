from django.shortcuts import render, render_to_response, RequestContext,HttpResponseRedirect
from djhelmet.forms import Admin_login, add_product
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User, Group

@login_required
def home(request):
    print "hello"
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))


def admin_login(request):
    form=Admin_login()
    if request.POST:
        print "Check"
        form=Admin_login(request.POST)
        if form.is_valid():
            print "Ha..ha..!!"
            username    = form.cleaned_data['username']
            password    = form.cleaned_data['password']
            print username
            print password
            flag_password=0
            user = auth.authenticate(username=username, password=password)
            print auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect("/admin_home/")
                else:
                    messages.warning(request,(("Unauthorized Entry..!! You do not have access to enter here...!!!")),fail_silently = True)

            else:
                 flag_password=1

            if flag_password == 1:
                messages.warning(request,(("Wrong Password")),fail_silently = True)

    return render_to_response('admin_login.html', locals(), context_instance = RequestContext(request))

@login_required
def admin_home(request):

    return render_to_response('admin_index.html', locals(), context_instance = RequestContext(request))

@login_required
def add_helmet(request):
    form=add_product()
    if request.POST:
        form=add_product(request.POST,request.FILES)
    if form.is_valid():
        print "Test"

    return render_to_response('add_helmet.html', locals(), context_instance = RequestContext(request))
from django.shortcuts import render, render_to_response, RequestContext,HttpResponseRedirect
from djhelmet.forms import Admin_login, add_product
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User, Group
from djhelmet.models import Colors, Product, Product_colors, Product_size, Size, Images
from random import randint

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
    colors = Colors.objects.all()
    #print colors
    form=add_product()
    if request.POST:
        form=add_product(request.POST,request.FILES)
    if form.is_valid():
        add_helmet=Product()
        add_size=Product_size()
        add_color=Product_colors()
        add_picture=Images()
        random_id=generate_random_id()
        add_helmet.product_id=random_id
        add_helmet.product_category="Helmet"
        add_helmet.product_brand_name = form.cleaned_data['product_brand_name']
        add_helmet.product_model_name = form.cleaned_data['product_model_name']
        add_helmet.price = form.cleaned_data['price']
        add_helmet.save()
        add_details=Product.objects.get(product_id=random_id)
        check=add_details
        color = form.cleaned_data['product_color']
        for available_colors in colors:
            color_check=Colors.objects.get(color=available_colors)
            add_color.product_id=check
            add_color.color=color_check
            add_color.save()
        size = form.cleaned_data['product_size']
        for available_size in size:
            size_check=Size.objects.get(size=available_size)
            add_size.product_id=check
            add_size.size=size_check
            add_size.save()
        add_picture.product_id=check
        add_picture.title = form.cleaned_data['product_model_name']
        add_picture.product_images = request.FILES['picture']
        add_picture.save()

    return render_to_response('add_helmet.html', locals(), context_instance = RequestContext(request))


def generate_random_id():
    id=randint(1000,99999)
    check_id = 0
    try:
        check_id=Product.objects.get(product_id=id)
    except:
        pass
    if id==check_id:
        generate_random_id()
    else:
        return id
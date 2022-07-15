from tokenize import group
from django.shortcuts import render, redirect
import sys

from dashboard.models import CrudOpr
from .forms import CrudForm, CreateUserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from .Middleware.auth import unauthenticated_user, allowed_users,admin_only

from django.contrib import messages
# Create your views here.




# sign up view
@unauthenticated_user
def SignUp(request):
    form = CreateUserForm()
    if request.method == 'POST':
        print("post data are", request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            # get user group name from 
            group = Group.objects.get(name='visiter')
            # add user into group
            user.groups.add(group)

            messages.success(request,'Account was created for ' + username)
            return redirect('login_page')
        else:    
            messages.error(request,form.errors)
    context = {'form': form}
    return render(request, "dashboard/sign_up.html", context)



# login
@unauthenticated_user
def Login(request):    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Username OR Password is not matched')    
    context = {}
    return render(request, "dashboard/login.html", context)



# logout functionality
@login_required(login_url='login_page')
def LogoutFunc(request):
    print("logout data", request)
    request.session.clear()
    logout(request)
    return redirect('login_page')



# index view
@login_required(login_url='login_page')
#@allowed_users(allowed_roles=['admin'])
def IndexView(request):
    return render(request, "dashboard/content.html")



# list view of crud
@login_required(login_url='login_page')
def CrudOprListView(request):
    data = CrudOpr.objects.all()
    context = {'object_list': data}
    print(context)
    return render(request, 'crud_opr/crud_opr_list.html',context)



# detail data
@login_required(login_url='login_page')
def CrudOprDetailView(request, pk):
    model = CrudOpr.objects.get(id=pk)
    context = {'object': model}
    print(context)
    return render(request, 'crud_opr/crud_opr_detail.html', context)



# create crud data
@login_required(login_url='login_page')
@allowed_users(allowed_roles=['admin'])
#@admin_only
def CrudOprCreateView(request):
    form = CrudForm()
    if request.method == 'POST':
        form = CrudForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/crud_opr/list')

    context = {'form': form}
    return render(request, 'crud_opr/crud_opr_create.html', context)



# edit crud data
@login_required(login_url='login_page')
def CrudOprUpdateView(request, pk):
    data = CrudOpr.objects.get(id=pk)
    # pass instance to pre-fill data
    form = CrudForm(instance=data)

    if request.method == 'POST':
        # send instance to upddate data
        form = CrudForm(request.POST, request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/crud_opr/list')

    context = {'form': form}
    return render(request, 'crud_opr/crud_opr_update.html', context)



# delete crud
@login_required(login_url='login_page')
def CrudOprDeleteView(request, pk):
    model = CrudOpr.objects.get(id=pk)

    if request.method == 'POST':
        model.delete()
        return redirect('/crud_opr/list')

    context = {'item': model}
    return render(request, 'crud_opr/crud_opr_delete.html', context)

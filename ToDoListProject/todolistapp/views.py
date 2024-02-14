from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm
from todolistapp.models import Task

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
# signup page
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



# logout page
def logout(request):
    return redirect('login')

# def task(request):
#     return render(request, 'task.html')

# Example in todolistapp/views.py


def index(request):
    context = {'success': False}
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        new_task = Task(title=title, description=description)
        new_task.save()
    return render(request, "index.html")


def task(request):
    tasks = Task.objects.all()
    print(tasks)
    context = {'tasks': tasks}
    for item in tasks:
        print(item.title)
    return render(request, 'task.html',context)
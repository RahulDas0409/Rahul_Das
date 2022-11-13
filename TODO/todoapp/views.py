from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from todoapp.models import Todo
from todoapp.forms import TodoForm

# Create your views here.
def index(request):
    todo = Todo.objects.all()
    context = {"todos":todo}
    return render(request, "index.html", context)

def addtodos(request):
    form = TodoForm()
    if request.method =="POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {"form":form}
    return render(request, "addtodos.html", context)

def updatetodos(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form":form}
    return render(request, "update_todo.html", context)

def deletetodos(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        todo.delete()
        return redirect("/")
    context = {'todo':todo}
    return render(request, "deletetodo.html", context)

def signin(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for" + user)
            return redirect("Log In")
    context = {"form":form}
    return render(request, "signin.html", context)

def log_in(request):
    if request.user.is_authenticated:
        return redirect("Home")
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, "You are now logged in as {username}.")
                    return redirect("Home")
                else:
                    messages.error(request, "Username or password is incorrect")
            else:
                messages.error(request, "Username or password is incorrect")
        form = AuthenticationForm()
        context={"form":form}
        return render(request, "login.html", context)

def log_out(request):
    logout(request)
    return redirect("Log In")
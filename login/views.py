from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, "index.html", context)

def registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect("/")

    else:
        if request.method == "POST":
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
            print(pw_hash)
            new_user = User.objects.create(
                first_name = request.POST['first_name'], 
                last_name = request.POST['last_name'], 
                email = request.POST['email'],
                password = pw_hash)
            request.session['user_id'] = new_user.id
            messages.success(request, "You have successfully registered!")
            return redirect("/main")

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    errors = {}
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            context = {
                'first_name': logged_user.first_name
            }
            return redirect('/main')
        else:
            errors['password'] = "Wrong password! Try again."
    else:
        errors['email'] = "No such email registered. Try again."
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect("/")

def logout(request):
    request.session.flush()
    return redirect("/") 
    
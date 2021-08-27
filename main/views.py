from django.shortcuts import render, redirect
from django.contrib import messages
from login.models import *
from .models import *
#from .forms import *

def main(request):
    if 'user_id' not in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session['user_id'])
    all_games = Game.objects.all().order_by('-date')

    context = {
        'user': user,
        'all_games': all_games,
    }
    return render(request, 'main.html', context)

def create(request):
    if 'user_id' not in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session['user_id'])

    if request.method == "POST":
        new_game = Game.objects.create(
            host_id = user,
            title = request.POST['title'],
            date = request.POST['date'],
            address = request.POST['address'],
            type = request.POST['type'],
            buyIn = request.POST['buyIn'],
            blinds = request.POST['blinds'],
            numberOfPlayers = request.POST['numberOfPlayers'],
            desc = request.POST['desc'])
        new_game.players.add(user)
        new_game.save()
        return redirect("/main")
    
    context = {
        'user': user,
    }

    return render(request, 'create.html', context)

def game(request, id):
    user = User.objects.get(id=request.session['user_id'])
    game = Game.objects.get(id = id)
    players = game.players.all()
    context = {
        'game': game,
        'players': players,
        'user': user,
    }
    if request.method == "GET":
        return render(request, "game.html", context)

def destroy(request, id):
    Game.objects.get(id = id).delete()
    return redirect("/main/")

def joinGame(request, id):
    user = User.objects.get(id=request.session['user_id'])
    game = Game.objects.get(id = id)
    
    if request.method == "POST":
        game.players.add(user)
        game.save()
        return redirect("/main/"+ str(game.id)+ '/')

def leaveGame(request, id):
    user = User.objects.get(id=request.session['user_id'])
    game = Game.objects.get(id = id)

    if request.method == "POST":
        game.players.remove(user)
        game.save()
        return redirect("/main/"+ str(game.id)+ '/')

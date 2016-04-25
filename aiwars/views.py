from django.shortcuts import render
from aiwars.models import Game
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import users

@login_required
def selectGame(request):
    all_games = Game.objects.all()
    context = {'game_list': all_games}
    return render(request,'aiwars/selectGame.html',context)

@login_required
def game(request,id):
    game = get_object_or_404(Game,pk=id)
    context = {'game': game}
    return render(request,'aiwars/game.html',context)
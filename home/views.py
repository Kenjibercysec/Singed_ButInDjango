from django.shortcuts import render
from django.http import HttpResponse
from .models import Dispositivos
# Create your views here.
def home(request):
    if request.method =="GET":
        return render(request, 'home.html')
    else:
        nome = request.POST.get('id_tombamento')

        user = Dispositivos(
            nome=nome
            )
        user.save()
        return HttpResponse(f'Olá, {nome}!')
    
##def cadpc(request):
  ##  if request.method =="GET":
    ##    return render(request, 'cadpc.html')
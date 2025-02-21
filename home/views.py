from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
# Create your views here.
def home(request):
    if request.method =="GET":
        return render(request, 'home.html')
    else:
        nome = request.POST.get('name')

        user = Usuario(
            nome=nome
            )
        user.save()
        return HttpResponse(f'Olá, {nome}!')